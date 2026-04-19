import { config } from './config'

/**
 * 发送消息给 Coze API（通过 Vercel 代理，解决 CORS）
 * API Token 由服务端环境变量注入，前端不传敏感信息
 */
export async function sendMessage(userMessage: string, conversationId?: string): Promise<string> {
  if (!config.botId) {
    return 'AI 聊天功能正在配置中，请稍后再来～\n\n其他功能（课表、集市、发现等）均可正常使用 🎓'
  }

  try {
    const response = await fetch(config.proxyUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        userId: config.userId || 'user_001',
        userMessage,
        ...(conversationId ? { conversationId } : {}),
      }),
    })

    if (!response.ok) {
      console.error('Proxy request failed:', response.status)
      return 'AI 聊天功能暂时不可用，请稍后再试 🙏'
    }

    const data = await response.json()
    return data.reply || '小轩暂时无法回复～'
  } catch (e: any) {
    console.error('Coze API error:', e)
    return 'AI 聊天功能暂时不可用，请稍后再试 🙏'
  }
}
