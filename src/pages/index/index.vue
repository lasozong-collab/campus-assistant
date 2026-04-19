<template>
  <view class="index-page">
    <!-- 顶部区域 -->
    <view class="header gradient-bg">
      <view class="header-content">
        <view class="greeting">
          <text class="greeting-text">{{ greeting }}，同学 👋</text>
          <text class="greeting-sub">今天也要元气满满哦</text>
        </view>
        <view class="header-right">
          <view class="avatar-wrapper">
            <text class="avatar-icon">👤</text>
          </view>
          <view class="bell" @tap="showToast('暂无新通知')">
            <text class="bell-icon">🔔</text>
            <view class="badge"></view>
          </view>
        </view>
      </view>
    </view>

    <!-- 搜索框 -->
    <view class="search-bar card" @tap="goChat">
      <text class="search-icon">🔍</text>
      <text class="search-placeholder">问我任何校园问题</text>
    </view>

    <!-- 快捷入口 -->
    <view class="shortcuts card">
      <view class="shortcut-grid">
        <view class="shortcut-item" v-for="item in shortcuts" :key="item.text" @tap="item.action">
          <view class="shortcut-icon">{{ item.icon }}</view>
          <text class="shortcut-text">{{ item.text }}</text>
        </view>
      </view>
    </view>

    <!-- 今日课表 -->
    <view class="section">
      <view class="section-header">
        <text class="section-title">📚 今日课表</text>
        <text class="section-more" @tap="switchTab('/pages/schedule/index')">查看全部 ></text>
      </view>
      <view class="today-schedule">
        <view class="schedule-item" v-for="item in todayCourses" :key="item.name"
              :style="{ borderLeftColor: item.color }">
          <view class="schedule-info">
            <text class="course-name">{{ item.name }}</text>
            <text class="course-detail">{{ item.time }} · {{ item.location }}</text>
          </view>
          <view class="course-status" :class="{ active: item.active }">
            <text class="status-text">{{ item.active ? '进行中' : '未开始' }}</text>
          </view>
        </view>
      </view>
    </view>

    <!-- 热门话题 -->
    <view class="section">
      <view class="section-header">
        <text class="section-title">🔥 热门话题</text>
      </view>
      <view class="topic-list">
        <view class="topic-card card" v-for="topic in topics" :key="topic.title" @tap="showToast(topic.title)">
          <text class="topic-title">{{ topic.title }}</text>
          <text class="topic-desc">{{ topic.desc }}</text>
          <view class="topic-meta">
            <text class="topic-views">{{ topic.views }} 浏览</text>
            <text class="topic-comments">{{ topic.comments }} 评论</text>
          </view>
        </view>
      </view>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

/** 根据时段返回问候语 */
const greeting = computed(() => {
  const h = new Date().getHours()
  if (h < 6) return '夜深了'
  if (h < 9) return '早上好'
  if (h < 12) return '上午好'
  if (h < 14) return '中午好'
  if (h < 18) return '下午好'
  return '晚上好'
})

/** 快捷入口 */
const shortcuts = ref([
  { icon: '📅', text: '课表', action: () => switchTab('/pages/schedule/index') },
  { icon: '📊', text: '成绩', action: () => showToast('成绩查询功能开发中') },
  { icon: '📰', text: '通知', action: () => showToast('暂无新通知') },
  { icon: '🏪', text: '集市', action: () => switchTab('/pages/market/index') },
  { icon: '📦', text: '快递', action: () => showToast('快递功能开发中') },
  { icon: '🤖', text: 'AI问答', action: () => goChat() },
])

/** 今日课程 */
const todayCourses = ref([
  { name: '高等数学', time: '08:00-09:40', location: '教学楼A301', color: '#4F6EF7', active: false },
  { name: '大学英语', time: '10:00-11:40', location: '外语楼B205', color: '#7C5CFC', active: true },
  { name: '数据结构', time: '14:00-15:40', location: '计算机楼C102', color: '#00C9A7', active: false },
])

/** 热门话题 */
const topics = ref([
  { title: '期末考试时间安排公布', desc: '教务处发布本学期期末考试安排，请注意查收...', views: 2341, comments: 186 },
  { title: '校园美食节即将开幕', desc: '第五届校园美食节将于本周六在东食堂广场举行...', views: 1856, comments: 92 },
  { title: '图书馆延长开放时间', desc: '考试季期间图书馆开放时间延长至晚上11点...', views: 3201, comments: 245 },
])

/** 跳转到TabBar页面 */
function switchTab(url: string) {
  uni.switchTab({ url })
}

/** 跳转到AI对话页 */
function goChat() {
  uni.navigateTo({ url: '/pages/chat/index' })
}

/** 显示提示 */
function showToast(msg: string) {
  uni.showToast({ title: msg, icon: 'none' })
}
</script>

<style scoped>
.index-page { padding-bottom: 20rpx; }

.header {
  padding: 60rpx 32rpx 40rpx;
  padding-top: calc(var(--status-bar-height, 44px) + 20rpx);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.greeting-text { font-size: 36rpx; font-weight: 700; color: #fff; display: block; }
.greeting-sub { font-size: 24rpx; color: rgba(255,255,255,0.8); margin-top: 8rpx; display: block; }

.header-right { display: flex; align-items: center; gap: 20rpx; }
.avatar-wrapper {
  width: 72rpx; height: 72rpx; border-radius: 50%;
  background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center;
}
.avatar-icon { font-size: 36rpx; }
.bell { position: relative; padding: 10rpx; }
.bell-icon { font-size: 36rpx; }
.badge {
  position: absolute; top: 4rpx; right: 4rpx;
  width: 14rpx; height: 14rpx; border-radius: 50%;
  background: var(--accent);
}

.search-bar {
  margin: -20rpx 24rpx 0;
  display: flex; align-items: center; gap: 16rpx;
  padding: 20rpx 24rpx; position: relative; z-index: 10;
}
.search-icon { font-size: 28rpx; }
.search-placeholder { color: var(--text-muted); font-size: 26rpx; }

.shortcuts { margin: 20rpx 24rpx; }
.shortcut-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 20rpx;
}
.shortcut-item {
  display: flex; flex-direction: column; align-items: center; gap: 12rpx;
  padding: 20rpx 0;
}
.shortcut-icon { font-size: 48rpx; }
.shortcut-text { font-size: 24rpx; color: var(--text-secondary); }

.section { margin-top: 20rpx; }
.section-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 0 24rpx 16rpx;
}
.section-title { font-size: 32rpx; font-weight: 600; }
.section-more { font-size: 24rpx; color: var(--primary); }

.today-schedule { padding: 0 24rpx; }
.schedule-item {
  background: var(--card); border-radius: var(--radius);
  box-shadow: var(--shadow); padding: 24rpx;
  margin-bottom: 16rpx; border-left: 6rpx solid;
  display: flex; justify-content: space-between; align-items: center;
}
.course-name { font-size: 28rpx; font-weight: 600; display: block; }
.course-detail { font-size: 22rpx; color: var(--text-muted); margin-top: 8rpx; display: block; }
.course-status {
  padding: 8rpx 20rpx; border-radius: 20rpx;
  background: var(--bg); font-size: 22rpx; color: var(--text-muted);
}
.course-status.active { background: rgba(79,110,247,0.1); color: var(--primary); }

.topic-list { padding: 0 24rpx; }
.topic-card { margin-bottom: 16rpx; }
.topic-title { font-size: 28rpx; font-weight: 600; display: block; }
.topic-desc {
  font-size: 24rpx; color: var(--text-secondary);
  margin-top: 12rpx; display: block;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.topic-meta { display: flex; gap: 24rpx; margin-top: 16rpx; }
.topic-views, .topic-comments { font-size: 22rpx; color: var(--text-muted); }
</style>
