<template>
  <view class="profile-page">
    <!-- 顶部 -->
    <view class="header gradient-bg">
      <view class="header-inner">
        <view class="avatar-large">
          <text class="avatar-emoji">🧑‍🎓</text>
        </view>
        <text class="user-name">Flechazo</text>
        <text class="user-id">学号：2023001XXXX</text>
      </view>
    </view>

    <!-- 统计卡片 -->
    <view class="stats card" style="margin-top: -30rpx; position: relative; z-index: 10;">
      <view class="stat-item">
        <text class="stat-num">12</text>
        <text class="stat-label">收藏</text>
      </view>
      <view class="stat-divider"></view>
      <view class="stat-item">
        <text class="stat-num">5</text>
        <text class="stat-label">发布</text>
      </view>
      <view class="stat-divider"></view>
      <view class="stat-item">
        <text class="stat-num">28</text>
        <text class="stat-label">获赞</text>
      </view>
    </view>

    <!-- 功能列表 -->
    <view class="menu-section">
      <view class="menu-card card">
        <view class="menu-item" v-for="item in menuList" :key="item.text" @tap="showToast(item.text)">
          <text class="menu-icon">{{ item.icon }}</text>
          <text class="menu-text">{{ item.text }}</text>
          <text class="menu-arrow">›</text>
        </view>
      </view>
    </view>

    <view class="footer-text">
      <text class="version">校园助手 v1.0.0</text>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const menuList = ref([
  { icon: '📅', text: '我的课表' },
  { icon: '⭐', text: '我的收藏' },
  { icon: '💬', text: '意见反馈' },
  { icon: 'ℹ️', text: '关于我们' },
  { icon: '⚙️', text: '设置' },
])

function showToast(msg: string) {
  uni.showToast({ title: msg, icon: 'none' })
}
</script>

<style scoped>
.profile-page { min-height: 100vh; background: var(--bg); }

.header {
  padding: calc(var(--status-bar-height, 44px) + 40rpx) 32rpx 60rpx;
  display: flex; flex-direction: column; align-items: center;
}
.avatar-large {
  width: 128rpx; height: 128rpx; border-radius: 50%;
  background: rgba(255,255,255,0.2); display: flex;
  align-items: center; justify-content: center;
  border: 4rpx solid rgba(255,255,255,0.4);
}
.avatar-emoji { font-size: 64rpx; }
.user-name { font-size: 36rpx; font-weight: 700; color: #fff; margin-top: 20rpx; }
.user-id { font-size: 24rpx; color: rgba(255,255,255,0.7); margin-top: 8rpx; }

.stats {
  display: flex; align-items: center; justify-content: space-around;
  padding: 32rpx 0; margin-left: 24rpx; margin-right: 24rpx;
}
.stat-item { display: flex; flex-direction: column; align-items: center; gap: 8rpx; }
.stat-num { font-size: 36rpx; font-weight: 700; color: var(--primary); }
.stat-label { font-size: 22rpx; color: var(--text-muted); }
.stat-divider { width: 1rpx; height: 60rpx; background: var(--border); }

.menu-section { margin-top: 24rpx; }
.menu-card { padding: 0; overflow: hidden; margin: 0 24rpx; }
.menu-item {
  display: flex; align-items: center; gap: 20rpx;
  padding: 28rpx 24rpx; border-bottom: 1rpx solid var(--border);
}
.menu-item:last-child { border-bottom: none; }
.menu-icon { font-size: 36rpx; }
.menu-text { flex: 1; font-size: 28rpx; }
.menu-arrow { font-size: 32rpx; color: var(--text-muted); }

.footer-text { text-align: center; padding: 40rpx 0 60rpx; }
.version { font-size: 22rpx; color: var(--text-muted); }
</style>
