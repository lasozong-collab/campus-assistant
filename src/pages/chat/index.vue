<template>
  <view class="chat-page">
    <!-- 导航栏 -->
    <view class="nav gradient-bg">
      <view class="nav-content">
        <view class="nav-back tap-scale" @tap="goBack">
          <text class="back-icon">←</text>
        </view>
        <view class="nav-center">
          <view class="bot-avatar">
            <text>🤖</text>
          </view>
          <view class="nav-info">
            <text class="nav-title">小轩</text>
            <view class="online-dot" :class="{ online: !loading }">
              <text class="online-text">{{ loading ? '思考中...' : '在线' }}</text>
            </view>
          </view>
        </view>
        <view style="width: 60rpx;"></view>
      </view>
    </view>

    <!-- 消息列表 -->
    <scroll-view class="message-list" scroll-y :scroll-top="scrollTop" :scroll-with-animation="true">
      <!-- 欢迎消息 -->
      <view class="msg-wrapper ai slide-up" v-if="messages.length === 0">
        <view class="msg-avatar-wrap">
          <text class="msg-avatar">🤖</text>
        </view>
        <view class="msg-bubble ai-bubble">
          <text class="msg-name">小轩</text>
          <text class="msg-text">你好！我是校园助手小轩 🎓\n\n你可以问我关于选课、成绩、图书馆、社团活动、奖学金等任何校园问题哦～</text>
        </view>
      </view>

      <view v-for="(msg, i) in messages" :key="i"
            class="msg-wrapper"
            :class="msg.role"
            :style="{ animationDelay: msg.role === 'user' ? '0s' : '0.1s' }">
        <view class="msg-avatar-wrap" v-if="msg.role === 'assistant'">
          <text class="msg-avatar">🤖</text>
        </view>
        <view class="msg-bubble" :class="msg.role === 'user' ? 'user-bubble' : 'ai-bubble'">
          <text class="msg-name" v-if="msg.role === 'assistant'">小轩</text>
          <text class="msg-text" :user-select="msg.role === 'assistant'">{{ msg.content }}</text>
        </view>
      </view>

      <!-- 加载动画 - 更精致 -->
      <view class="msg-wrapper ai" v-if="loading">
        <view class="msg-avatar-wrap">
          <text class="msg-avatar">🤖</text>
        </view>
        <view class="msg-bubble ai-bubble">
          <view class="typing-indicator">
            <view class="typing-dot"></view>
            <view class="typing-dot"></view>
            <view class="typing-dot"></view>
          </view>
        </view>
      </view>
    </scroll-view>

    <!-- 推荐问题 -->
    <view class="suggestions" v-if="messages.length === 0 && !loading">
      <scroll-view scroll-x class="suggestions-scroll" :show-scrollbar="false">
        <view class="sug-tag tap-scale" v-for="(tag, idx) in suggestionTags" :key="tag"
              :style="{ animationDelay: idx * 0.08 + 's' }"
              @tap="sendTagMessage(tag)">
          <text class="sug-text">{{ tag }}</text>
        </view>
      </scroll-view>
    </view>

    <!-- 输入框 -->
    <view class="input-bar">
      <view class="input-wrapper">
        <input class="input" v-model="inputText" placeholder="输入你的问题..."
               confirm-type="send" @confirm="sendMessage" :disabled="loading" />
        <view class="send-btn" :class="{ active: inputText.trim() && !loading }"
              @tap="sendMessage">
          <text class="send-icon">↑</text>
        </view>
      </view>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue'
import { sendMessage as cozeSend } from '@/api/coze'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

const messages = ref<Message[]>([])
const inputText = ref('')
const loading = ref(false)
const scrollTop = ref(0)
const conversationId = ref('')

const suggestionTags = ['选课攻略', '成绩查询', '图书馆', '奖学金', '社团推荐', '考研指南']

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

function sendTagMessage(tag: string) {
  inputText.value = tag
  sendMessage()
}

function scrollToBottom() {
  nextTick(() => { scrollTop.value = 99999 })
}

function goBack() {
  uni.navigateBack()
}
</script>

<style scoped>
.chat-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: var(--bg);
}

/* 导航栏 */
.nav {
  padding: 0 24rpx;
  padding-top: calc(var(--status-bar-height, 44px) + 10rpx);
  padding-bottom: 24rpx;
}

.nav-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 1;
}

.nav-back {
  width: 64rpx;
  height: 64rpx;
  border-radius: 50%;
  background: rgba(255,255,255,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
}

.back-icon {
  font-size: 36rpx;
  color: #fff;
  font-weight: 700;
}

.nav-center {
  display: flex;
  align-items: center;
  gap: 14rpx;
}

.bot-avatar {
  width: 56rpx;
  height: 56rpx;
  border-radius: 18rpx;
  background: rgba(255,255,255,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28rpx;
}

.nav-info {
  display: flex;
  flex-direction: column;
}

.nav-title {
  font-size: 30rpx;
  font-weight: 700;
  color: #fff;
}

.online-dot {
  display: flex;
  align-items: center;
  gap: 6rpx;
  margin-top: 2rpx;
}

.online-dot::before {
  content: '';
  width: 10rpx;
  height: 10rpx;
  border-radius: 50%;
  background: rgba(255,255,255,0.5);
}

.online-dot.online::before {
  background: #34D399;
  animation: pulse 2s infinite;
}

.online-text {
  font-size: 20rpx;
  color: rgba(255,255,255,0.7);
}

/* 消息列表 */
.message-list {
  flex: 1;
  padding: 24rpx;
  overflow-y: auto;
}

.msg-wrapper {
  display: flex;
  align-items: flex-start;
  gap: 16rpx;
  margin-bottom: 28rpx;
  animation: slideUp 0.35s ease-out both;
}

.msg-wrapper.user {
  flex-direction: row-reverse;
}

.msg-avatar-wrap {
  width: 64rpx;
  height: 64rpx;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.msg-avatar {
  font-size: 28rpx;
}

.msg-bubble {
  max-width: 72%;
  padding: 20rpx 28rpx;
  border-radius: var(--radius-lg);
}

.ai-bubble {
  background: var(--card);
  box-shadow: var(--shadow-sm);
  border-top-left-radius: 8rpx;
}

.user-bubble {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: #fff;
  border-top-right-radius: 8rpx;
}

.msg-name {
  font-size: 20rpx;
  color: var(--text-muted);
  margin-bottom: 8rpx;
  display: block;
  font-weight: 500;
}

.msg-text {
  font-size: 28rpx;
  line-height: 1.7;
  white-space: pre-wrap;
  word-break: break-all;
}

/* 加载动画 - 更精致的三点跳动 */
.typing-indicator {
  display: flex;
  gap: 10rpx;
  padding: 8rpx 0;
}

.typing-dot {
  width: 16rpx;
  height: 16rpx;
  border-radius: 50%;
  background: var(--primary);
  animation: typingBounce 1.4s ease-in-out infinite;
}

.typing-dot:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typingBounce {
  0%, 60%, 100% {
    transform: translateY(0);
    opacity: 0.4;
  }
  30% {
    transform: translateY(-10rpx);
    opacity: 1;
  }
}

/* 推荐标签 */
.suggestions {
  padding: 12rpx 24rpx;
  background: var(--bg);
  border-top: 1rpx solid var(--border);
}

.suggestions-scroll {
  white-space: nowrap;
}

.sug-tag {
  display: inline-block;
  padding: 14rpx 32rpx;
  background: var(--card);
  border-radius: 36rpx;
  margin-right: 16rpx;
  box-shadow: var(--shadow-sm);
  border: 1rpx solid var(--border);
  animation: slideUp 0.4s ease-out both;
}

.sug-text {
  font-size: 24rpx;
  color: var(--text-secondary);
  font-weight: 500;
}

/* 输入栏 */
.input-bar {
  padding: 16rpx 24rpx;
  padding-bottom: calc(16rpx + env(safe-area-inset-bottom));
  background: var(--card);
  border-top: 1rpx solid var(--border);
}

.input-wrapper {
  display: flex;
  align-items: center;
  gap: 12rpx;
  background: var(--bg);
  border-radius: 48rpx;
  padding: 8rpx 8rpx 8rpx 28rpx;
  border: 1rpx solid var(--border);
}

.input {
  flex: 1;
  height: 72rpx;
  font-size: 28rpx;
}

.send-btn {
  width: 64rpx;
  height: 64rpx;
  border-radius: 50%;
  background: var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  flex-shrink: 0;
}

.send-btn.active {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  transform: scale(1.05);
  box-shadow: 0 4rpx 16rpx rgba(99,102,241,0.3);
}

.send-icon {
  font-size: 30rpx;
  color: #fff;
  font-weight: 700;
}

.send-btn:not(.active) .send-icon {
  color: var(--text-muted);
}
</style>
