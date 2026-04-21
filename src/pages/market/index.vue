<template>
  <view class="market-page">
    <!-- 顶部 -->
    <view class="header gradient-bg">
      <view class="header-inner">
        <text class="header-title">校园集市</text>
        <text class="header-sub">闲置好物 · 校园互助</text>
      </view>
      <!-- 分类Tab -->
      <scroll-view scroll-x class="tabs-scroll" :show-scrollbar="false">
        <view class="tab tap-scale" v-for="tab in tabs" :key="tab"
              :class="{ active: activeTab === tab }" @tap="activeTab = tab">
          <text class="tab-text">{{ tab }}</text>
        </view>
      </scroll-view>
    </view>

    <!-- 信息流 -->
    <scroll-view class="feed" scroll-y>
      <view class="feed-card card tap-scale slide-up"
            v-for="(item, idx) in filteredItems" :key="item.id"
            :style="{ animationDelay: idx * 0.08 + 's' }">
        <view class="feed-header">
          <view class="author-avatar" :style="{ background: item.avatarBg }">
            <text class="avatar-emoji">{{ item.avatar }}</text>
          </view>
          <view class="author-info">
            <text class="author-name">{{ item.author }}</text>
            <text class="publish-time">{{ item.time }}</text>
          </view>
          <view class="category-tag" :style="{ background: getCategoryColor(item.category) }">
            <text class="category-text">{{ item.category }}</text>
          </view>
        </view>
        <text class="feed-title">{{ item.title }}</text>
        <text class="feed-desc">{{ item.desc }}</text>
        <view class="feed-footer">
          <text class="feed-price" v-if="item.price">{{ item.price }}</text>
          <view class="feed-actions">
            <view class="action-btn tap-scale" @tap="showToast('已点赞')">
              <text class="action-icon">👍</text>
              <text class="action-num">{{ item.likes }}</text>
            </view>
            <view class="action-btn tap-scale" @tap="showToast('评论功能开发中')">
              <text class="action-icon">💬</text>
              <text class="action-num">{{ item.comments }}</text>
            </view>
          </view>
        </view>
      </view>
      <view style="height: 180rpx;"></view>
    </scroll-view>

    <!-- 悬浮发布按钮 -->
    <view class="fab tap-scale" @tap="showToast('发布功能开发中')" style="animation: float 3s ease-in-out infinite;">
      <text class="fab-icon">+</text>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

const activeTab = ref('全部')
const tabs = ['全部', '二手交易', '失物招领', '代取快递']

interface MarketItem {
  id: number
  avatar: string
  avatarBg: string
  author: string
  time: string
  category: string
  title: string
  desc: string
  price?: string
  likes: number
  comments: number
}

const items = ref<MarketItem[]>([
  { id: 1, avatar: '👩', avatarBg: 'linear-gradient(135deg, #F43F5E, #FB7185)', author: '小美', time: '10分钟前', category: '二手交易', title: '九成新iPad Air5', desc: '去年买的，贴膜保护完好，128G蓝色，因换新机出', price: '¥2,800', likes: 23, comments: 8 },
  { id: 2, avatar: '👦', avatarBg: 'linear-gradient(135deg, #3B82F6, #60A5FA)', author: '阿强', time: '30分钟前', category: '失物招领', title: '捡到一张校园卡', desc: '在图书馆三楼捡到的，姓名看起来是"王同学"，请联系认领', likes: 5, comments: 2 },
  { id: 3, avatar: '👧', avatarBg: 'linear-gradient(135deg, #8B5CF6, #A78BFA)', author: '学霸姐', time: '1小时前', category: '二手交易', title: '考研全套资料打包出', desc: '包含数学一、英语一、政治全套教材和真题，附赠笔记', price: '¥80', likes: 45, comments: 19 },
  { id: 4, avatar: '🧑', avatarBg: 'linear-gradient(135deg, #10B981, #34D399)', author: '快递达人', time: '2小时前', category: '代取快递', title: '代取菜鸟驿站快递', desc: '长期代取，5元/件，当天下单当天送达，校内免配送费', likes: 12, comments: 6 },
  { id: 5, avatar: '👩', avatarBg: 'linear-gradient(135deg, #F59E0B, #FBBF24)', author: '小姐姐', time: '3小时前', category: '二手交易', title: '全新Nike运动鞋', desc: '买小了一码穿不了，42码，全新带吊牌', price: '¥350', likes: 31, comments: 14 },
  { id: 6, avatar: '👦', avatarBg: 'linear-gradient(135deg, #0EA5E9, #38BDF8)', author: '理工男', time: '4小时前', category: '失物招领', title: '在食堂丢了一个水杯', desc: '蓝色保温杯，上面有贴纸，有看到的同学请私信，必有重谢！', likes: 3, comments: 1 },
  { id: 7, avatar: '🧑', avatarBg: 'linear-gradient(135deg, #EC4899, #F472B6)', author: '跑腿小哥', time: '5小时前', category: '代取快递', title: '代购代拿服务', desc: '可以代买奶茶、零食、日用品，校内配送15分钟达', likes: 8, comments: 3 },
  { id: 8, avatar: '👧', avatarBg: 'linear-gradient(135deg, #6366F1, #818CF8)', author: '学姐', time: '6小时前', category: '二手交易', title: '专业课本低价转让', desc: '计算机专业大三全部课本，每本20元，全套打包100', price: '¥20/本', likes: 56, comments: 22 },
])

const filteredItems = computed(() => {
  if (activeTab.value === '全部') return items.value
  return items.value.filter(i => i.category === activeTab.value)
})

function getCategoryColor(cat: string) {
  const colors: Record<string, string> = {
    '二手交易': 'rgba(99,102,241,0.08)',
    '失物招领': 'rgba(244,63,94,0.08)',
    '代取快递': 'rgba(16,185,129,0.08)',
  }
  return colors[cat] || 'var(--bg)'
}

function showToast(msg: string) {
  uni.showToast({ title: msg, icon: 'none' })
}
</script>

<style scoped>
.market-page {
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

.tabs-scroll {
  padding: 0 24rpx;
  white-space: nowrap;
  position: relative;
  z-index: 1;
}

.tab {
  display: inline-block;
  padding: 12rpx 32rpx;
  border-radius: 36rpx;
  background: rgba(255,255,255,0.12);
  margin-right: 16rpx;
  transition: all 0.25s ease;
}

.tab.active {
  background: rgba(255,255,255,0.95);
  box-shadow: 0 4rpx 12rpx rgba(0,0,0,0.08);
}

.tab-text {
  font-size: 24rpx;
  color: rgba(255,255,255,0.85);
  font-weight: 500;
}

.tab.active .tab-text {
  color: var(--primary);
  font-weight: 700;
}

.feed {
  flex: 1;
  padding: 20rpx 24rpx;
}

.feed-card {
  margin-bottom: 20rpx;
}

.feed-header {
  display: flex;
  align-items: center;
  gap: 16rpx;
  margin-bottom: 16rpx;
}

.author-avatar {
  width: 72rpx;
  height: 72rpx;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.avatar-emoji { font-size: 32rpx; }

.author-info { flex: 1; }

.author-name {
  font-size: 26rpx;
  font-weight: 700;
  display: block;
}

.publish-time {
  font-size: 20rpx;
  color: var(--text-muted);
  display: block;
  margin-top: 2rpx;
}

.category-tag {
  padding: 6rpx 16rpx;
  border-radius: 8rpx;
}

.category-text {
  font-size: 20rpx;
  color: var(--primary);
  font-weight: 600;
}

.feed-title {
  font-size: 30rpx;
  font-weight: 700;
  display: block;
  margin-bottom: 8rpx;
  line-height: 1.4;
}

.feed-desc {
  font-size: 24rpx;
  color: var(--text-muted);
  display: block;
  margin-bottom: 16rpx;
  line-height: 1.6;
}

.feed-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.feed-price {
  font-size: 32rpx;
  font-weight: 800;
  color: var(--accent);
}

.feed-actions {
  display: flex;
  gap: 24rpx;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 6rpx;
}

.action-icon { font-size: 24rpx; }

.action-num {
  font-size: 24rpx;
  color: var(--text-muted);
}

.fab {
  position: fixed;
  right: 40rpx;
  bottom: 200rpx;
  width: 104rpx;
  height: 104rpx;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8rpx 32rpx rgba(99,102,241,0.4);
}

.fab-icon {
  font-size: 52rpx;
  color: #fff;
  font-weight: 300;
}
</style>
