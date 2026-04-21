<template>
  <view class="discover-page">
    <!-- 顶部 -->
    <view class="header gradient-bg">
      <view class="header-inner">
        <text class="header-title">发现</text>
        <text class="header-sub">探索校园精彩内容</text>
      </view>
      <!-- 搜索框 -->
      <view class="search-box glass" @tap="showToast('搜索功能开发中')">
        <text class="search-icon">🔍</text>
        <text class="search-placeholder">搜索校园攻略...</text>
      </view>
      <!-- 分类 -->
      <scroll-view scroll-x class="category-scroll" :show-scrollbar="false">
        <view class="category tap-scale" v-for="cat in categories" :key="cat"
              :class="{ active: activeCategory === cat }" @tap="activeCategory = cat">
          <text class="category-text">{{ cat }}</text>
        </view>
      </scroll-view>
    </view>

    <!-- 文章列表 -->
    <scroll-view class="article-list" scroll-y>
      <view class="article-card tap-scale slide-up"
            v-for="(item, idx) in filteredArticles" :key="item.id"
            :style="{ animationDelay: idx * 0.08 + 's' }"
            @tap="showToast('文章详情开发中')">
        <view class="article-cover" :style="{ background: item.coverColor }">
          <text class="cover-emoji">{{ item.emoji }}</text>
        </view>
        <view class="article-content">
          <text class="article-title">{{ item.title }}</text>
          <text class="article-summary">{{ item.summary }}</text>
          <view class="article-meta">
            <view class="article-tag" :style="{ background: item.tagColor }">
              <text class="tag-text">{{ item.tag }}</text>
            </view>
            <text class="meta-info">{{ item.author }} · {{ item.views }}阅读</text>
          </view>
        </view>
      </view>
      <view style="height: 180rpx;"></view>
    </scroll-view>
  </view>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

const activeCategory = ref('全部')
const categories = ['全部', '学习', '生活', '活动', '美食']

interface Article {
  id: number
  title: string
  summary: string
  emoji: string
  coverColor: string
  tag: string
  tagColor: string
  author: string
  views: string
}

const articles = ref<Article[]>([
  { id: 1, title: '大一新生选课全攻略', summary: '手把手教你如何选课，避开坑课，选到心仪的老师', emoji: '📚', coverColor: 'linear-gradient(135deg, #6366F1, #8B5CF6)', tag: '学习', tagColor: 'rgba(99,102,241,0.1)', author: '学长说', views: '2.3万' },
  { id: 2, title: '校园周边美食地图', summary: '东门到西门，最值得吃的20家店全在这', emoji: '🍜', coverColor: 'linear-gradient(135deg, #F43F5E, #FB7185)', tag: '美食', tagColor: 'rgba(244,63,94,0.1)', author: '吃货小分队', views: '1.8万' },
  { id: 3, title: '社团招新指南2025', summary: '30+社团详细介绍，找到最适合你的组织', emoji: '🎭', coverColor: 'linear-gradient(135deg, #3B82F6, #06B6D4)', tag: '活动', tagColor: 'rgba(59,130,246,0.1)', author: '学生会', views: '3.1万' },
  { id: 4, title: '图书馆生存手册', summary: '预约技巧、最佳座位、充电位置全部公开', emoji: '📖', coverColor: 'linear-gradient(135deg, #10B981, #34D399)', tag: '学习', tagColor: 'rgba(16,185,129,0.1)', author: '学霸联盟', views: '1.5万' },
  { id: 5, title: '宿舍好物推荐清单', summary: '提升宿舍生活品质的30件神器', emoji: '🏠', coverColor: 'linear-gradient(135deg, #F59E0B, #FBBF24)', tag: '生活', tagColor: 'rgba(245,158,11,0.1)', author: '生活达人', views: '2.7万' },
  { id: 6, title: '奖学金申请全流程', summary: '国奖、校奖、企业奖，一篇搞懂申请流程', emoji: '🏆', coverColor: 'linear-gradient(135deg, #8B5CF6, #A78BFA)', tag: '学习', tagColor: 'rgba(139,92,246,0.1)', author: '资助中心', views: '4.2万' },
  { id: 7, title: '校运动会报名指南', summary: '项目介绍、报名方式、训练计划一应俱全', emoji: '🏃', coverColor: 'linear-gradient(135deg, #F97316, #FB923C)', tag: '活动', tagColor: 'rgba(249,115,22,0.1)', author: '体育部', views: '8600' },
  { id: 8, title: '食堂窗口评分排行', summary: '全校6个食堂最火窗口TOP20', emoji: '🍽️', coverColor: 'linear-gradient(135deg, #0EA5E9, #38BDF8)', tag: '美食', tagColor: 'rgba(14,165,233,0.1)', author: '美食团', views: '3.5万' },
])

const filteredArticles = computed(() => {
  if (activeCategory.value === '全部') return articles.value
  return articles.value.filter(a => a.tag === activeCategory.value)
})

function showToast(msg: string) {
  uni.showToast({ title: msg, icon: 'none' })
}
</script>

<style scoped>
.discover-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: var(--bg);
}

.header {
  padding-top: calc(var(--status-bar-height, 44px) + 24rpx);
  padding-bottom: 28rpx;
}

.header-inner {
  padding: 0 32rpx 20rpx;
  position: relative;
  z-index: 1;
}

.header-title {
  font-size: 40rpx;
  font-weight: 700;
  color: #fff;
  display: block;
}

.header-sub {
  font-size: 24rpx;
  color: rgba(255,255,255,0.7);
  margin-top: 4rpx;
  display: block;
}

.search-box {
  margin: 0 24rpx 20rpx;
  padding: 16rpx 24rpx;
  border-radius: 48rpx;
  display: flex;
  align-items: center;
  gap: 12rpx;
  position: relative;
  z-index: 1;
}

.search-placeholder {
  color: var(--text-secondary);
  font-size: 26rpx;
}

.category-scroll {
  padding: 0 24rpx;
  white-space: nowrap;
  position: relative;
  z-index: 1;
}

.category {
  display: inline-block;
  padding: 12rpx 32rpx;
  border-radius: 36rpx;
  background: rgba(255,255,255,0.12);
  margin-right: 16rpx;
  transition: all 0.25s ease;
}

.category.active {
  background: rgba(255,255,255,0.95);
  box-shadow: 0 4rpx 12rpx rgba(0,0,0,0.08);
}

.category-text {
  font-size: 24rpx;
  color: rgba(255,255,255,0.85);
  font-weight: 500;
}

.category.active .category-text {
  color: var(--primary);
  font-weight: 700;
}

.article-list {
  flex: 1;
  padding: 20rpx 24rpx;
}

.article-card {
  display: flex;
  gap: 24rpx;
  background: var(--card);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  margin-bottom: 20rpx;
  padding: 20rpx;
  overflow: hidden;
  border: 1rpx solid var(--border);
}

.article-cover {
  width: 180rpx;
  height: 180rpx;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.cover-emoji { font-size: 56rpx; }

.article-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-width: 0;
}

.article-title {
  font-size: 28rpx;
  font-weight: 700;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  display: block;
  line-height: 1.4;
}

.article-summary {
  font-size: 22rpx;
  color: var(--text-muted);
  margin-top: 8rpx;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.6;
}

.article-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 8rpx;
}

.article-tag {
  padding: 4rpx 14rpx;
  border-radius: 8rpx;
}

.tag-text {
  font-size: 20rpx;
  color: var(--primary);
  font-weight: 600;
}

.meta-info {
  font-size: 20rpx;
  color: var(--text-muted);
}
</style>
