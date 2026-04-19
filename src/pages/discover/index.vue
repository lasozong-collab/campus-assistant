<template>
  <view class="discover-page">
    <!-- 顶部 -->
    <view class="header gradient-bg">
      <view class="header-inner">
        <text class="header-title">🔍 发现</text>
      </view>
      <!-- 搜索框 -->
      <view class="search-box" @tap="showToast('搜索功能开发中')">
        <text class="search-icon">🔍</text>
        <text class="search-placeholder">搜索校园攻略...</text>
      </view>
      <!-- 分类 -->
      <scroll-view scroll-x class="category-scroll">
        <view class="category" v-for="cat in categories" :key="cat"
              :class="{ active: activeCategory === cat }" @tap="activeCategory = cat">
          <text class="category-text">{{ cat }}</text>
        </view>
      </scroll-view>
    </view>

    <!-- 文章列表 -->
    <scroll-view class="article-list" scroll-y>
      <view class="article-card" v-for="item in filteredArticles" :key="item.id" @tap="showToast('文章详情开发中')">
        <view class="article-cover" :style="{ background: item.coverColor }">
          <text class="cover-emoji">{{ item.emoji }}</text>
        </view>
        <view class="article-content">
          <text class="article-title">{{ item.title }}</text>
          <text class="article-summary">{{ item.summary }}</text>
          <view class="article-meta">
            <view class="article-tag">
              <text class="tag-text">{{ item.tag }}</text>
            </view>
            <text class="meta-info">{{ item.author }} · {{ item.views }}阅读</text>
          </view>
        </view>
      </view>
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
  author: string
  views: string
}

const articles = ref<Article[]>([
  { id: 1, title: '大一新生选课全攻略', summary: '手把手教你如何选课，避开坑课，选到心仪的老师', emoji: '📚', coverColor: 'linear-gradient(135deg, #667eea, #764ba2)', tag: '学习', author: '学长说', views: '2.3万' },
  { id: 2, title: '校园周边美食地图', summary: '东门到西门，最值得吃的20家店全在这', emoji: '🍜', coverColor: 'linear-gradient(135deg, #f093fb, #f5576c)', tag: '美食', author: '吃货小分队', views: '1.8万' },
  { id: 3, title: '社团招新指南2025', summary: '30+社团详细介绍，找到最适合你的组织', emoji: '🎭', coverColor: 'linear-gradient(135deg, #4facfe, #00f2fe)', tag: '活动', author: '学生会', views: '3.1万' },
  { id: 4, title: '图书馆生存手册', summary: '预约技巧、最佳座位、充电位置全部公开', emoji: '📖', coverColor: 'linear-gradient(135deg, #43e97b, #38f9d7)', tag: '学习', author: '学霸联盟', views: '1.5万' },
  { id: 5, title: '宿舍好物推荐清单', summary: '提升宿舍生活品质的30件神器', emoji: '🏠', coverColor: 'linear-gradient(135deg, #fa709a, #fee140)', tag: '生活', author: '生活达人', views: '2.7万' },
  { id: 6, title: '奖学金申请全流程', summary: '国奖、校奖、企业奖，一篇搞懂申请流程', emoji: '🏆', coverColor: 'linear-gradient(135deg, #a18cd1, #fbc2eb)', tag: '学习', author: '资助中心', views: '4.2万' },
  { id: 7, title: '校运动会报名指南', summary: '项目介绍、报名方式、训练计划一应俱全', emoji: '🏃', coverColor: 'linear-gradient(135deg, #ffecd2, #fcb69f)', tag: '活动', author: '体育部', views: '8600' },
  { id: 8, title: '食堂窗口评分排行', summary: '全校6个食堂最火窗口TOP20', emoji: '🍽️', coverColor: 'linear-gradient(135deg, #89f7fe, #66a6ff)', tag: '美食', author: '美食团', views: '3.5万' },
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
.discover-page { display: flex; flex-direction: column; height: 100vh; background: var(--bg); }
.header { padding-top: calc(var(--status-bar-height, 44px) + 20rpx); padding-bottom: 24rpx; }
.header-inner { padding: 0 32rpx 20rpx; }
.header-title { font-size: 36rpx; font-weight: 700; color: #fff; }

.search-box {
  margin: 0 24rpx 20rpx; padding: 16rpx 24rpx;
  background: rgba(255,255,255,0.2); border-radius: 30rpx;
  display: flex; align-items: center; gap: 12rpx;
}
.search-placeholder { color: rgba(255,255,255,0.7); font-size: 26rpx; }

.category-scroll { padding: 0 24rpx; white-space: nowrap; }
.category {
  display: inline-block; padding: 10rpx 28rpx;
  border-radius: 30rpx; background: rgba(255,255,255,0.15);
  margin-right: 16rpx; transition: all 0.2s;
}
.category.active { background: rgba(255,255,255,0.9); }
.category-text { font-size: 24rpx; color: rgba(255,255,255,0.9); }
.category.active .category-text { color: var(--primary); font-weight: 600; }

.article-list { flex: 1; padding: 20rpx 24rpx; }
.article-card {
  display: flex; gap: 20rpx; background: var(--card);
  border-radius: var(--radius); box-shadow: var(--shadow);
  margin-bottom: 20rpx; padding: 20rpx; overflow: hidden;
}
.article-cover {
  width: 180rpx; height: 180rpx; border-radius: 12rpx;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.cover-emoji { font-size: 60rpx; }
.article-content { flex: 1; display: flex; flex-direction: column; justify-content: space-between; min-width: 0; }
.article-title {
  font-size: 28rpx; font-weight: 600;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  display: block;
}
.article-summary {
  font-size: 22rpx; color: var(--text-secondary); margin-top: 8rpx;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;
  overflow: hidden;
}
.article-meta { display: flex; align-items: center; justify-content: space-between; margin-top: 8rpx; }
.article-tag { padding: 4rpx 12rpx; background: rgba(79,110,247,0.1); border-radius: 6rpx; }
.tag-text { font-size: 20rpx; color: var(--primary); }
.meta-info { font-size: 20rpx; color: var(--text-muted); }
</style>
