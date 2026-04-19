# 🎓 校园助手

基于 **uni-app (Vue 3 + TypeScript)** 的智能校园服务小程序/H5，AI 对话功能由 **扣子 (Coze)** 驱动。

## 功能

- 🏠 **首页** — 快捷入口、今日课表、热门话题
- 📅 **课表** — 周视图课表，支持切换周次
- 🏪 **集市** — 二手交易、失物招领、代取快递
- 🔍 **发现** — 校园攻略、美食推荐、活动资讯
- 💬 **AI 问答** — 基于 Coze Bot 的智能校园助手
- 👤 **我的** — 个人中心

## 技术栈

- Vue 3 + TypeScript + Pinia
- uni-app（支持微信小程序 + H5）
- Vite 构建
- Vercel 部署（H5）

## 本地开发

```bash
# H5 开发
npm run dev:h5

# 微信小程序开发
npm run dev:mp-weixin
```

## 部署

项目已配置 Vercel 部署：

1. 代码推到 GitHub
2. 在 [Vercel](https://vercel.com) 导入仓库
3. 自动构建部署

### AI 聊天配置

编辑 `src/api/config.ts`，填入你的 Coze Bot 信息：

```ts
export const config = {
  botId: '你的 Bot ID',
  apiToken: '你的 API Token',
  proxyUrl: '/api/coze-proxy',
  userId: 'user_001',
}
```

> ⚠️ API Token 通过 Vercel 代理转发，不会直接暴露在前端。
> 但当前版本 Token 仍在 `config.ts` 中明文配置，正式使用建议改为 Vercel 环境变量。

## License

MIT
