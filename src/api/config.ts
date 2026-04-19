/**
 * Coze API 配置
 * 前端不再直连 Coze，而是走 Vercel Serverless 代理（解决 CORS）
 */
export const config = {
  /** Coze Bot ID */
  botId: '7625170677502918656',
  /** Coze API Token — 通过 Vercel 环境变量 COZE_API_TOKEN 注入，不在前端暴露 */
  apiToken: '', // 部署时在 Vercel 设置环境变量 COZE_API_TOKEN
  /** Vercel 代理地址（部署后会自动指向 /api/coze-proxy） */
  proxyUrl: '/api/coze-proxy',
  /** 用户ID */
  userId: 'user_001',
}
