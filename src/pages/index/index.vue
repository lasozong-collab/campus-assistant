<template>
  <view class="index-page">
    <!-- 顶部 Hero 区域 -->
    <view class="hero gradient-bg">
      <view class="hero-content">
        <view class="hero-top">
          <view class="greeting-area">
            <text class="greeting-text">{{ greeting }}，Flechazo 👋</text>
            <text class="greeting-sub">今天也要元气满满哦</text>
          </view>
          <view class="hero-right">
            <view class="bell tap-scale" @tap="showToast('暂无新通知')">
              <text class="bell-icon">🔔</text>
              <view class="badge"></view>
            </view>
          </view>
        </view>

        <!-- 搜索框 - 毛玻璃风格 -->
        <view class="search-bar glass tap-scale" @tap="goChat">
          <text class="search-icon">✨</text>
          <text class="search-placeholder">问我任何校园问题...</text>
          <view class="search-btn">
            <text class="search-btn-text">→</text>
          </view>
        </view>
      </view>
    </view>

    <!-- 快捷入口 - 横向滚动卡片 -->
    <view class="shortcuts-section">
      <scroll-view scroll-x class="shortcuts-scroll" :show-scrollbar="false">
        <view class="shortcut-card tap-scale" v-for="(item, idx) in shortcuts" :key="item.text"
              :style="{ animationDelay: idx * 0.08 + 's' }"
              @tap="item.action">
          <view class="shortcut-icon-wrap" :style="{ background: item.bgColor }">
            <text class="shortcut-icon">{{ item.icon }}</text>
          </view>
          <text class="shortcut-text">{{ item.text }}</text>
        </view>
      </scroll-view>
    </view>

    <!-- AI 聊天入口 Banner -->
    <view class="ai-banner card tap-scale" @tap="goChat" style="animation-delay: 0.2s;">
      <view class="ai-banner-left">
        <view class="ai-avatar" style="animation: float 3s ease-in-out infinite;">
          <text>🤖</text>
        </view>
        <view class="ai-info">
          <text class="ai-title">AI 校园助手</text>
          <text class="ai-desc">选课、成绩、生活问题随时问我</text>
        </view>
      </view>
      <view class="ai-go">
        <text class="ai-go-text">去聊聊</text>
      </view>
    </view>

    <!-- 今日课表 -->
    <view class="section slide-up" style="animation-delay: 0.3s;">
      <view class="section-header">
        <view class="section-title-wrap">
          <text class="section-title">📚 今日课表</text>
          <view class="course-count">
            <text class="count-text">{{ todayCourses.length }}节课</text>
          </view>
        </view>
        <text class="section-more tap-scale" @tap="switchTab('/pages/schedule/index')">全部 ›</text>
      </view>
      <view class="today-schedule">
        <view class="schedule-card card tap-scale" v-for="(item, idx) in todayCourses" :key="item.name"
              :style="{ animationDelay: idx * 0.1 + 's' }">
          <view class="schedule-color-bar" :style="{ background: item.color }"></view>
          <view class="schedule-body">
            <view class="schedule-info">
              <text class="course-name">{{ item.name }}</text>
              <text class="course-detail">{{ item.time }}</text>
            </view>
            <view class="schedule-location">
              <text class="location-text">📍 {{ item.location }}</text>
            </view>
            <view class="course-status" :class="{ active: item.active, ended: item.ended }">
              <text class="status-text">{{ item.active ? '进行中' : item.ended ? '已结束' : '未开始' }}</text>
            </view>
          </view>
        </view>
      </view>
    </view>

    <!-- 热门话题 -->
    <view class="section slide-up" style="animation-delay: 0.4s;">
      <view class="section-header">
        <text class="section-title">🔥 热门话题</text>
        <text class="section-more tap-scale" @tap="switchTab('/pages/discover/index')">更多 ›</text>
      </view>
      <view class="topic-list">
        <view class="topic-card card tap-scale" v-for="(topic, idx) in topics" :key="topic.title"
              :style="{ animationDelay: idx * 0.1 + 's' }"
              @tap="showToast(topic.title)">
          <view class="topic-content">
            <view class="topic-badge" :style="{ background: topic.badgeColor }">
              <text class="badge-text">{{ topic.badge }}</text>
            </view>
            <text class="topic-title">{{ topic.title }}</text>
            <text class="topic-desc">{{ topic.desc }}</text>
          </view>
          <view class="topic-stats">
            <view class="stat-row">
              <text class="stat-icon">👁</text>
              <text class="stat-num">{{ topic.views }}</text>
            </view>
            <view class="stat-row">
              <text class="stat-icon">💬</text>
              <text class="stat-num">{{ topic.comments }}</text>
            </view>
          </view>
        </view>
      </view>
    </view>

    <!-- 底部留白 -->
    <view style="height: 180rpx;"></view>
  </view>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

const greeting = computed(() => {
  const h = new Date().getHours()
  if (h < 6) return '夜深了'
  if (h < 9) return '早上好'
  if (h < 12) return '上午好'
  if (h < 14) return '中午好'
  if (h < 18) return '下午好'
  return '晚上好'
})

const shortcuts = ref([
  { icon: '📅', text: '课表', action: () => switchTab('/pages/schedule/index'), bgColor: 'rgba(99,102,241,0.12)' },
  { icon: '📊', text: '成绩', action: () => showToast('成绩查询功能开发中'), bgColor: 'rgba(16,185,129,0.12)' },
  { icon: '📰', text: '通知', action: () => showToast('暂无新通知'), bgColor: 'rgba(244,63,94,0.12)' },
  { icon: '🏪', text: '集市', action: () => switchTab('/pages/market/index'), bgColor: 'rgba(245,158,11,0.12)' },
  { icon: '📦', text: '快递', action: () => showToast('快递功能开发中'), bgColor: 'rgba(139,92,246,0.12)' },
  { icon: '🤖', text: 'AI问答', action: () => goChat(), bgColor: 'rgba(99,102,241,0.12)' },
  { icon: '🏃', text: '操场', action: () => showToast('操场预约开发中'), bgColor: 'rgba(16,185,129,0.12)' },
  { icon: '📚', text: '图书馆', action: () => showToast('图书馆功能开发中'), bgColor: 'rgba(245,158,11,0.12)' },
])

const todayCourses = ref([
  { name: '高等数学', time: '08:00 - 09:40', location: '教学楼A301', color: '#6366F1', active: false, ended: true },
  { name: '大学英语', time: '10:00 - 11:40', location: '外语楼B205', color: '#8B5CF6', active: true, ended: false },
  { name: '数据结构', time: '14:00 - 15:40', location: '计算机楼C102', color: '#10B981', active: false, ended: false },
])

const topics = ref([
  { title: '期末考试时间安排公布', desc: '教务处发布本学期期末考试安排，请注意查收', views: '2341', comments: '186', badge: '教务', badgeColor: 'rgba(99,102,241,0.1)' },
  { title: '校园美食节即将开幕', desc: '第五届校园美食节将于本周六在东食堂广场举行', views: '1856', comments: '92', badge: '活动', badgeColor: 'rgba(244,63,94,0.1)' },
  { title: '图书馆延长开放时间', desc: '考试季期间图书馆开放时间延长至晚上11点', views: '3201', comments: '245', badge: '通知', badgeColor: 'rgba(16,185,129,0.1)' },
])

function switchTab(url: string) {
  uni.switchTab({ url })
}

function goChat() {
  uni.navigateTo({ url: '/pages/chat/index' })
}

function showToast(msg: string) {
  uni.showToast({ title: msg, icon: 'none' })
}
</script>

<style scoped>
.index-page {
  padding-bottom: 20rpx;
  min-height: 100vh;
}

/* Hero 顶部 */
.hero {
  padding: 60rpx 32rpx 56rpx;
  padding-top: calc(var(--status-bar-height, 44px) + 24rpx);
}

.hero-content {
  position: relative;
  z-index: 1;
}

.hero-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.greeting-text {
  font-size: 40rpx;
  font-weight: 700;
  color: #fff;
  display: block;
  letter-spacing: 1rpx;
}

.greeting-sub {
  font-size: 24rpx;
  color: rgba(255,255,255,0.75);
  margin-top: 8rpx;
  display: block;
}

.hero-right {
  display: flex;
  align-items: center;
}

.bell {
  position: relative;
  width: 76rpx;
  height: 76rpx;
  border-radius: 50%;
  background: rgba(255,255,255,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
}

.bell-icon { font-size: 36rpx; }

.badge {
  position: absolute;
  top: 12rpx;
  right: 12rpx;
  width: 16rpx;
  height: 16rpx;
  border-radius: 50%;
  background: var(--accent);
  border: 3rpx solid rgba(255,255,255,0.8);
}

/* 搜索框 */
.search-bar {
  margin-top: 32rpx;
  display: flex;
  align-items: center;
  gap: 16rpx;
  padding: 20rpx 28rpx;
  border-radius: 60rpx;
  margin-left: 0;
  margin-right: 0;
}

.search-icon { font-size: 28rpx; }

.search-placeholder {
  color: var(--text-secondary);
  font-size: 26rpx;
  flex: 1;
}

.search-btn {
  width: 56rpx;
  height: 56rpx;
  border-radius: 50%;
  background: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-btn-text {
  color: #fff;
  font-size: 28rpx;
  font-weight: 600;
}

/* 快捷入口 */
.shortcuts-section {
  padding: 24rpx 0;
}

.shortcuts-scroll {
  padding: 0 24rpx;
  white-space: nowrap;
}

.shortcut-card {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 12rpx;
  width: 140rpx;
  margin-right: 20rpx;
  padding: 24rpx 0;
  background: var(--card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  animation: slideUp 0.4s ease-out both;
  vertical-align: top;
}

.shortcut-icon-wrap {
  width: 80rpx;
  height: 80rpx;
  border-radius: 24rpx;
  display: flex;
  align-items: center;
  justify-content: center;
}

.shortcut-icon { font-size: 40rpx; }

.shortcut-text {
  font-size: 24rpx;
  color: var(--text-secondary);
  font-weight: 500;
}

/* AI Banner */
.ai-banner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 28rpx 32rpx;
  background: linear-gradient(135deg, #EEF2FF 0%, #F5F3FF 100%);
  border: 1rpx solid rgba(99,102,241,0.15);
  animation: slideUp 0.5s ease-out both;
}

.ai-banner-left {
  display: flex;
  align-items: center;
  gap: 20rpx;
}

.ai-avatar {
  width: 80rpx;
  height: 80rpx;
  border-radius: 24rpx;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 40rpx;
}

.ai-title {
  font-size: 28rpx;
  font-weight: 700;
  color: var(--text);
  display: block;
}

.ai-desc {
  font-size: 22rpx;
  color: var(--text-muted);
  margin-top: 4rpx;
  display: block;
}

.ai-go {
  padding: 12rpx 28rpx;
  background: var(--primary);
  border-radius: 30rpx;
}

.ai-go-text {
  color: #fff;
  font-size: 24rpx;
  font-weight: 600;
}

/* Section 通用 */
.section {
  margin-top: 12rpx;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 32rpx 20rpx;
}

.section-title-wrap {
  display: flex;
  align-items: center;
  gap: 16rpx;
}

.section-title {
  font-size: 32rpx;
  font-weight: 700;
}

.course-count {
  padding: 4rpx 16rpx;
  background: rgba(99,102,241,0.08);
  border-radius: 20rpx;
}

.count-text {
  font-size: 20rpx;
  color: var(--primary);
  font-weight: 500;
}

.section-more {
  font-size: 24rpx;
  color: var(--text-muted);
}

/* 课表卡片 */
.today-schedule {
  padding: 0 24rpx;
}

.schedule-card {
  padding: 0;
  margin-bottom: 16rpx;
  overflow: hidden;
  animation: slideUp 0.5s ease-out both;
}

.schedule-body {
  display: flex;
  align-items: center;
  padding: 24rpx;
  gap: 20rpx;
}

.schedule-color-bar {
  width: 8rpx;
  height: 80rpx;
  border-radius: 4rpx;
  flex-shrink: 0;
}

.schedule-info {
  flex: 1;
}

.course-name {
  font-size: 28rpx;
  font-weight: 700;
  display: block;
}

.course-detail {
  font-size: 22rpx;
  color: var(--text-muted);
  margin-top: 6rpx;
  display: block;
}

.schedule-location {
  flex-shrink: 0;
}

.location-text {
  font-size: 22rpx;
  color: var(--text-secondary);
}

.course-status {
  padding: 8rpx 20rpx;
  border-radius: 20rpx;
  background: var(--bg);
  flex-shrink: 0;
}

.status-text {
  font-size: 20rpx;
  color: var(--text-muted);
  font-weight: 500;
}

.course-status.active {
  background: rgba(99,102,241,0.1);
}

.course-status.active .status-text {
  color: var(--primary);
}

.course-status.ended .status-text {
  color: var(--text-muted);
}

/* 热门话题 */
.topic-list {
  padding: 0 24rpx;
}

.topic-card {
  padding: 0;
  margin-bottom: 16rpx;
  overflow: hidden;
  animation: slideUp 0.5s ease-out both;
}

.topic-content {
  padding: 24rpx;
}

.topic-badge {
  display: inline-block;
  padding: 4rpx 16rpx;
  border-radius: 8rpx;
  margin-bottom: 12rpx;
}

.badge-text {
  font-size: 20rpx;
  font-weight: 600;
}

.topic-title {
  font-size: 28rpx;
  font-weight: 700;
  display: block;
  line-height: 1.4;
}

.topic-desc {
  font-size: 24rpx;
  color: var(--text-muted);
  margin-top: 8rpx;
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.topic-stats {
  display: flex;
  gap: 32rpx;
  padding: 16rpx 24rpx;
  background: var(--bg);
  border-top: 1rpx solid var(--border);
}

.stat-row {
  display: flex;
  align-items: center;
  gap: 8rpx;
}

.stat-icon { font-size: 22rpx; }

.stat-num {
  font-size: 22rpx;
  color: var(--text-muted);
}
</style>
