<template>
  <view class="chat-page">
    <!-- 导航栏 -->
    <view class="nav gradient-bg">
      <view class="nav-content">
        <view class="nav-back" @tap="goBack">
          <text class="back-icon">←</text>
        </view>
        <view class="nav-center">
          <view class="bot-avatar">🤖</view>
          <text class="nav-title">小轩</text>
        </view>
        <view style="width: 60rpx;"></view>
      </view>
    </view>

    <!-- 消息列表 -->
    <scroll-view class="message-list" scroll-y :scroll-top="scrollTop" :scroll-with-animation="true">
      <!-- 欢迎消息 -->
      <view class="msg-wrapper ai" v-if="messages.length === 0">
        <view class="msg-avatar">🤖</view>
        <view class="msg-bubble ai-bubble">
          <text class="msg-name">小轩</text>
          <text class="msg-text">你好！我是校园助手小轩 🎓\n\n你可以问我关于选课、成绩、图书馆、社团活动、奖学金等任何校园问题哦～</text>
        </view>
      </view>

      <view v-for="(msg, i) in messages" :key="i" class="msg-wrapper" :class="msg.role">
        <view class="msg-avatar" v-if="msg.role === 'assistant'">🤖</view>
        <view class="msg-bubble" :class="msg.role === 'user' ? 'user-bubble' : 'ai-bubble'">
          <text class="msg-name" v-if="msg.role === 'assistant'">小轩</text>
          <text class="msg-text" :user-select="msg.role === 'assistant'">{{ msg.content }}</text>
        </view>
      </view>

      <!-- 加载动画 -->
      <view class="msg-wrapper ai" v-if="loading">
        <view class="msg-avatar">🤖</view>
        <view class="msg-bubble ai-bubble">
          <view class="typing-dots">
            <view class="dot"></view>
            <view class="dot"></view>
            <view class="dot"></view>
          </view>
        </view>
      </view>
    </scroll-view>

    <!-- 推荐问题 -->
    <view class="suggestions" v-if="messages.length === 0 && !loading">
      <scroll-view scroll-x class="suggestions-scroll">
        <view class="tag" v-for="tag in suggestionTags" :key="tag" @tap="sendTagMessage(tag)">
          <text class="tag-text">{{ tag }}</text>
        </view>
      </scroll-view>
    </view>

    <!-- 输入框 -->
    <view class="input-bar">
      <view class="input-wrapper">
        <input class="input" v-model="inputText" placeholder="输入你的问题..." confirm-type="send"
               @confirm="sendMessage" :disabled="loading" />
        <view class="send-btn" :class="{ active: inputText.trim() && !loading }" @tap="sendMessage">
          <text class="send-icon">发送</text>
        </view>
      </view>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue'
import { sendMessage as cozeSend } from '@/api/coze'

/** 消息类型 */
interface Message {
  role: 'user' | 'assistant'
  content: string
}

const messages = ref<Message[]>([])
const inputText = ref('')
const loading = ref(false)
const scrollTop = ref(0)
const conversationId = ref('')

/** 推荐问题标签 */
const suggestionTags = ['选课攻略', '成绩查询', '图书馆', '奖学金', '社团推荐', '考研指南']

/** 发送消息 */
async function sendMessage() {
  const text = inputText.value.trim()
  if (!text || loading.value) return

  messages.value.push({ role: 'user', content: text })
  inputText.value = ''
  loading.value = true
  scrollToBottom()

  try {
    const reply = await cozeSend(text)
    messages.value.push({ role: 'assistant', content: reply })
  } catch (e: any) {
    messages.value.push({ role: 'assistant', content: '抱歉，出了点小问题，请稍后再试 🙏' })
  } finally {
    loading.value = false
    scrollToBottom()
  }
}

/** 点击推荐标签发送 */
function sendTagMessage(tag: string) {
  inputText.value = tag
  sendMessage()
}

/** 滚动到底部 */
function scrollToBottom() {
  nextTick(() => { scrollTop.value = 99999 })
}

/** 返回上一页 */
function goBack() {
  uni.navigateBack()
}
</script>

<style scoped>
.chat-page {
  display: flex; flex-direction: column; height: 100vh;
  background: var(--bg);
}

.nav {
  padding: 0 24rpx; padding-top: calc(var(--status-bar-height, 44px) + 10rpx);
  padding-bottom: 20rpx;
}
.nav-content { display: flex; align-items: center; justify-content: space-between; }
.nav-back { width: 60rpx; height: 60rpx; display: flex; align-items: center; justify-content: center; }
.back-icon { font-size: 36rpx; color: #fff; font-weight: 700; }
.nav-center { display: flex; align-items: center; gap: 12rpx; }
.bot-avatar { font-size: 36rpx; }
.nav-title { font-size: 32rpx; font-weight: 600; color: #fff; }

.message-list {
  flex: 1; padding: 24rpx; overflow-y: auto;
}

.msg-wrapper {
  display: flex; align-items: flex-start; gap: 16rpx;
  margin-bottom: 32rpx;
}
.msg-wrapper.user { flex-direction: row-reverse; }
.msg-avatar {
  width: 64rpx; height: 64rpx; border-radius: 50%;
  background: var(--bg); display: flex; align-items: center; justify-content: center;
  font-size: 32rpx; flex-shrink: 0;
}
.msg-bubble {
  max-width: 70%; padding: 20rpx 24rpx;
  border-radius: 16rpx;
}
.ai-bubble { background: var(--card); box-shadow: var(--shadow); border-top-left-radius: 4rpx; }
.user-bubble { background: var(--primary); color: #fff; border-top-right-radius: 4rpx; }
.msg-name { font-size: 22rpx; color: var(--text-muted); margin-bottom: 8rpx; display: block; }
.msg-text { font-size: 28rpx; line-height: 1.6; white-space: pre-wrap; word-break: break-all; }

/* 加载动画 */
.typing-dots { display: flex; gap: 8rpx; padding: 8rpx 0; }
.dot {
  width: 12rpx; height: 12rpx; border-radius: 50%;
  background: var(--text-muted); animation: bounce 1.4s infinite ease-in-out both;
}
.dot:nth-child(1) { animation-delay: -0.32s; }
.dot:nth-child(2) { animation-delay: -0.16s; }
@keyframes bounce {
  0%, 80%, 100% { transform: scale(0); }
  40% { transform: scale(1); }
}

/* 推荐标签 */
.suggestions { padding: 16rpx 24rpx; background: var(--bg); }
.suggestions-scroll { white-space: nowrap; }
.tag {
  display: inline-block; padding: 12rpx 28rpx;
  background: var(--card); border-radius: 30rpx;
  margin-right: 16rpx; box-shadow: var(--shadow);
}
.tag-text { font-size: 24rpx; color: var(--primary); }

/* 输入栏 */
.input-bar {
  padding: 16rpx 24rpx; padding-bottom: calc(16rpx + env(safe-area-inset-bottom));
  background: var(--card); border-top: 1rpx solid var(--border);
}
.input-wrapper {
  display: flex; align-items: center; gap: 16rpx;
  background: var(--bg); border-radius: 40rpx; padding: 8rpx 8rpx 8rpx 24rpx;
}
.input { flex: 1; height: 72rpx; font-size: 28rpx; }
.send-btn {
  padding: 12rpx 32rpx; border-radius: 30rpx;
  background: var(--border); transition: all 0.2s;
}
.send-btn.active { background: var(--primary); }
.send-icon { font-size: 26rpx; color: #fff; }
.send-btn:not(.active) .send-icon { color: var(--text-muted); }
</style>
