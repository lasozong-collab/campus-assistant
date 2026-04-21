<script setup lang="ts">
import { onLaunch } from '@dcloudio/uni-app'

onLaunch(() => {
  console.log('校园助手启动')
})
</script>

<style>
/* 全局CSS变量 - 现代主题 */
page {
  --primary: #6366F1;
  --primary-light: #818CF8;
  --secondary: #8B5CF6;
  --accent: #F43F5E;
  --accent-light: #FB7185;
  --success: #10B981;
  --warning: #F59E0B;
  --bg: #F8FAFC;
  --card: #FFFFFF;
  --text: #0F172A;
  --text-secondary: #475569;
  --text-muted: #94A3B8;
  --border: #E2E8F0;
  --shadow-sm: 0 1rpx 3rpx rgba(0, 0, 0, 0.04);
  --shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.06);
  --shadow-md: 0 8rpx 24rpx rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 16rpx 48rpx rgba(0, 0, 0, 0.12);
  --radius-sm: 12rpx;
  --radius: 20rpx;
  --radius-lg: 28rpx;
  --radius-xl: 36rpx;

  background-color: var(--bg);
  font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Segoe UI', Roboto, sans-serif;
  font-size: 28rpx;
  color: var(--text);
  -webkit-font-smoothing: antialiased;
}

/* 渐变背景 */
.gradient-bg {
  background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
  position: relative;
  overflow: hidden;
}

.gradient-bg::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -30%;
  width: 400rpx;
  height: 400rpx;
  border-radius: 50%;
  background: rgba(255,255,255,0.08);
}

.gradient-bg::after {
  content: '';
  position: absolute;
  bottom: -20%;
  left: -20%;
  width: 300rpx;
  height: 300rpx;
  border-radius: 50%;
  background: rgba(255,255,255,0.05);
}

/* 通用卡片 */
.card {
  background: var(--card);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 24rpx;
  margin: 20rpx 24rpx;
}

/* 毛玻璃效果 */
.glass {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20rpx);
  -webkit-backdrop-filter: blur(20rpx);
  border: 1rpx solid rgba(255, 255, 255, 0.3);
}

/* 页面切换动画 */
page {
  animation: pageIn 0.35s ease-out;
}

@keyframes pageIn {
  from {
    opacity: 0;
    transform: translateY(20rpx);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 通用过渡 */
.fade-in {
  animation: fadeIn 0.4s ease-out forwards;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(16rpx); }
  to { opacity: 1; transform: translateY(0); }
}

/* 弹性点击效果 */
.tap-scale {
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.tap-scale:active {
  transform: scale(0.96);
  box-shadow: var(--shadow-sm);
}

/* 脉冲动画 */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}

/* 浮动动画 */
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-12rpx); }
}

/* 渐入上移动画 - 用于列表项 */
@keyframes slideUp {
  from { opacity: 0; transform: translateY(24rpx); }
  to { opacity: 1; transform: translateY(0); }
}

.slide-up {
  animation: slideUp 0.5s ease-out forwards;
}

/* 骨架屏闪烁 */
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
</style>
