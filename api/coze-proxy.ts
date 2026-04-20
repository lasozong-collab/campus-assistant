declare const process: {
  env: Record<string, string | undefined>
}

/**
 * Vercel Serverless Function - Coze API 代理
 * 解决浏览器直接调用 Coze API 的 CORS 问题
 *
 * 安全说明：
 * - COZE_API_TOKEN 通过 Vercel 环境变量注入，不暴露在前端
 * - BOT_ID 同样通过环境变量注入
 */

export const config = {
  runtime: 'edge',
}

export default async function handler(req: Request) {
  // CORS 预检
  if (req.method === 'OPTIONS') {
    return new Response(null, {
      status: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      },
    })
  }

  // 只允许 POST
  if (req.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), {
      status: 405,
      headers: { 'Content-Type': 'application/json' },
    })
  }

  try {
    const body = await req.json()
    const { userId, userMessage, conversationId } = body

    // 从 Vercel 环境变量读取，前端不需要传
    const botId = process.env.BOT_ID || ''
    const apiToken = process.env.COZE_API_TOKEN || ''

    if (!botId || !apiToken) {
      return new Response(
        JSON.stringify({ reply: 'AI 聊天功能正在配置中，请稍后再来～', error: 'Server: Missing env vars' }),
        { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' } }
      )
    }

    if (!userMessage) {
      return new Response(
        JSON.stringify({ error: 'Missing userMessage' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      )
    }

    // 1. 发送消息给 Coze
    const chatResp = await fetch('https://api.coze.cn/v3/chat', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiToken}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        bot_id: botId,
        user_id: userId || 'user_001',
        stream: false,
        auto_save_history: true,
        additional_messages: [
          {
            role: 'user',
            content: userMessage,
            content_type: 'text',
          }
        ],
        ...(conversationId ? { conversation_id: conversationId } : {}),
      }),
    })

    if (!chatResp.ok) {
      const errText = await chatResp.text()
      console.error('Coze API error:', chatResp.status, errText)
      return new Response(
        JSON.stringify({ reply: 'AI 暂时不可用，请稍后再试 🙏', error: `Coze API ${chatResp.status}` }),
        { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' } }
      )
    }

    const chatData = await chatResp.json()

    if (chatData.code !== 0 || !chatData.data) {
      console.error('Coze API biz error:', chatData)
      const errMsg = chatData.msg || JSON.stringify(chatData)
      return new Response(
        JSON.stringify({ reply: `[调试] Coze错误: ${errMsg}`, error: 'Coze biz error', detail: chatData }),
        { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' } }
      )
    }

    const chatId = chatData.data.id
    const convId = chatData.data.conversation_id

    // 2. 轮询等待结果
    let attempts = 0
    const maxAttempts = 30
    while (attempts < maxAttempts) {
      await new Promise(r => setTimeout(r, 1000))

      const pollResp = await fetch(
        `https://api.coze.cn/v3/chat/retrieve?chat_id=${chatId}&conversation_id=${convId}`,
        { headers: { 'Authorization': `Bearer ${apiToken}` } }
      )
      const pollData = await pollResp.json()

      if (pollData.data && pollData.data.status === 'completed') {
        const lastMsg = pollData.data.messages?.find((m: any) => m.type === 'answer')
        return new Response(
          JSON.stringify({
            reply: lastMsg?.content || '暂时无法回复～',
            conversation_id: convId,
          }),
          {
            status: 200,
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
            },
          }
        )
      }

      if (pollData.data && (pollData.data.status === 'failed' || pollData.data.status === 'requires_action')) {
        return new Response(
          JSON.stringify({ reply: '暂时无法回复，请稍后再试 🙏', error: 'Chat failed' }),
          { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' } }
        )
      }

      attempts++
    }

    return new Response(
      JSON.stringify({ reply: '回复超时，请稍后再试 🙏', error: 'timeout' }),
      { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' } }
    )
  } catch (e: any) {
    console.error('Proxy error:', e)
    return new Response(
      JSON.stringify({ reply: 'AI 暂时不可用，请稍后再试 🙏', error: e.message }),
      { status: 500, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' } }
    )
  }
}
