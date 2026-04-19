<script setup lang="ts">
import { onLaunch } from '@dcloudio/uni-app'

onLaunch(() => {
  console.log('校园助手启动')
})
</script>

<style>
/* 全局CSS变量 - 主题色 */
page {
  --primary: #4F6EF7;
  --secondary: #7C5CFC;
  --accent: #FF6B6B;
  --bg: #F5F7FA;
  --card: #FFFFFF;
  --text: #333333;
  --text-secondary: #666666;
  --text-muted: #999999;
  --border: #EEEEEE;
  --shadow: 0 2rpx 12rpx rgba(0, 0, 0, 0.06);
  --radius: 16rpx;

  background-color: var(--bg);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 28rpx;
  color: var(--text);
}

/* 渐变背景 */
.gradient-bg {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
}

/* 通用卡片 */
.card {
  background: var(--card);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 24rpx;
  margin: 20rpx 24rpx;
}
</style>
