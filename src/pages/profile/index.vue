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
        <!-- 统计 -->
        <view class="header-stats">
          <view class="h-stat-item">
            <text class="h-stat-num">12</text>
            <text class="h-stat-label">收藏</text>
          </view>
          <view class="h-stat-divider"></view>
          <view class="h-stat-item">
            <text class="h-stat-num">5</text>
            <text class="h-stat-label">发布</text>
          </view>
          <view class="h-stat-divider"></view>
          <view class="h-stat-item">
            <text class="h-stat-num">28</text>
            <text class="h-stat-label">获赞</text>
          </view>
        </view>
      </view>
    </view>

    <!-- 功能卡片组 -->
    <view class="menu-section slide-up" style="animation-delay: 0.15s;">
      <view class="menu-card card">
        <view class="menu-item tap-scale" v-for="(item, idx) in menuList" :key="item.text"
              @tap="showToast(item.text)"
              :style="{ animationDelay: idx * 0.05 + 's' }">
          <view class="menu-icon-wrap" :style="{ background: item.iconBg }">
            <text class="menu-icon">{{ item.icon }}</text>
          </view>
          <text class="menu-text">{{ item.text }}</text>
          <text class="menu-arrow">›</text>
        </view>
      </view>
    </view>

    <!-- 关于卡片 -->
    <view class="about-card card slide-up" style="animation-delay: 0.3s;">
      <view class="about-content">
        <view class="about-logo">
          <text>🎓</text>
        </view>
        <text class="about-title">校园助手</text>
        <text class="about-desc">你的校园生活好帮手</text>
        <text class="about-version">v1.1.0</text>
      </view>
    </view>

    <view style="height: 180rpx;"></view>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const menuList = ref([
  { icon: '📅', text: '我的课表', iconBg: 'rgba(99,102,241,0.1)' },
  { icon: '⭐', text: '我的收藏', iconBg: 'rgba(245,158,11,0.1)' },
  { icon: '💬', text: '意见反馈', iconBg: 'rgba(16,185,129,0.1)' },
  { icon: 'ℹ️', text: '关于我们', iconBg: 'rgba(139,92,246,0.1)' },
  { icon: '⚙️', text: '设置', iconBg: 'rgba(100,116,139,0.1)' },
])

function showToast(msg: string) {
  uni.showToast({ title: msg, icon: 'none' })
}
</script>

<style scoped>
.profile-page {
  min-height: 100vh;
  background: var(--bg);
}

.header {
  padding: calc(var(--status-bar-height, 44px) + 40rpx) 32rpx 48rpx;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 1;
}

.avatar-large {
  width: 140rpx;
  height: 140rpx;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  border: 4rpx solid rgba(255,255,255,0.3);
}

.avatar-emoji { font-size: 68rpx; }

.user-name {
  font-size: 36rpx;
  font-weight: 800;
  color: #fff;
  margin-top: 20rpx;
  letter-spacing: 1rpx;
}

.user-id {
  font-size: 24rpx;
  color: rgba(255,255,255,0.65);
  margin-top: 6rpx;
}

.header-stats {
  display: flex;
  align-items: center;
  gap: 40rpx;
  margin-top: 28rpx;
  padding: 20rpx 40rpx;
  background: rgba(255,255,255,0.12);
  border-radius: 40rpx;
}

.h-stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4rpx;
}

.h-stat-num {
  font-size: 30rpx;
  font-weight: 800;
  color: #fff;
}

.h-stat-label {
  font-size: 20rpx;
  color: rgba(255,255,255,0.7);
}

.h-stat-divider {
  width: 1rpx;
  height: 40rpx;
  background: rgba(255,255,255,0.2);
}

.menu-section {
  margin-top: 24rpx;
}

.menu-card {
  padding: 0;
  overflow: hidden;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 20rpx;
  padding: 28rpx 28rpx;
  border-bottom: 1rpx solid var(--border);
  animation: slideUp 0.4s ease-out both;
}

.menu-item:last-child { border-bottom: none; }

.menu-icon-wrap {
  width: 72rpx;
  height: 72rpx;
  border-radius: 20rpx;
  display: flex;
  align-items: center;
  justify-content: center;
}

.menu-icon { font-size: 32rpx; }

.menu-text {
  flex: 1;
  font-size: 28rpx;
  font-weight: 500;
}

.menu-arrow {
  font-size: 32rpx;
  color: var(--text-muted);
}

.about-card {
  margin-top: 20rpx;
  text-align: center;
}

.about-content {
  padding: 16rpx 0;
}

.about-logo {
  font-size: 56rpx;
  margin-bottom: 12rpx;
}

.about-title {
  font-size: 30rpx;
  font-weight: 800;
  display: block;
}

.about-desc {
  font-size: 22rpx;
  color: var(--text-muted);
  margin-top: 4rpx;
  display: block;
}

.about-version {
  font-size: 20rpx;
  color: var(--text-muted);
  margin-top: 8rpx;
  display: block;
}
</style>
