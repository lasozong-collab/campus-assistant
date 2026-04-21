<template>
  <view class="schedule-page">
    <!-- 顶部 -->
    <view class="header gradient-bg">
      <view class="header-inner">
        <view class="header-left">
          <text class="header-title">我的课表</text>
        </view>
        <view class="week-selector">
          <view class="week-arrow tap-scale" @tap="changeWeek(-1)">
            <text class="arrow-text">‹</text>
          </view>
          <text class="week-text">第 {{ currentWeek }} 周</text>
          <view class="week-arrow tap-scale" @tap="changeWeek(1)">
            <text class="arrow-text">›</text>
          </view>
        </view>
      </view>
    </view>

    <!-- 星期头 -->
    <view class="weekdays">
      <view class="weekday" v-for="(d, i) in weekdays" :key="i"
            :class="{ active: i === todayIndex }">
        <text class="weekday-label">{{ d.label }}</text>
        <view class="weekday-date-wrap" :class="{ active: i === todayIndex }">
          <text class="weekday-date">{{ d.date }}</text>
        </view>
      </view>
    </view>

    <!-- 课表网格 -->
    <scroll-view class="timetable" scroll-y>
      <view class="time-grid">
        <view class="time-row" v-for="slot in timeSlots" :key="slot.period">
          <view class="time-label">
            <text class="period-text">第{{ slot.period }}节</text>
            <text class="time-text">{{ slot.time }}</text>
          </view>
          <view class="course-columns">
            <view class="course-cell tap-scale" v-for="(d, i) in weekdays" :key="i"
                  @tap="showDetail(getCourse(d.label, slot.period))">
              <view class="course-block" v-if="getCourse(d.label, slot.period)"
                    :style="{ background: getCourse(d.label, slot.period)!.color }">
                <text class="course-name">{{ getCourse(d.label, slot.period)!.name }}</text>
                <text class="course-room">{{ getCourse(d.label, slot.period)!.room }}</text>
              </view>
            </view>
          </view>
        </view>
      </view>
      <view style="height: 180rpx;"></view>
    </scroll-view>

    <!-- 课程详情弹窗 -->
    <view class="modal-mask" v-if="selectedCourse" @tap="selectedCourse = null">
      <view class="modal-content card" @tap.stop>
        <view class="modal-header">
          <text class="modal-title">{{ selectedCourse.name }}</text>
        </view>
        <view class="modal-body">
          <view class="info-item">
            <view class="info-icon-wrap">
              <text>📍</text>
            </view>
            <text class="info-text">{{ selectedCourse.room }}</text>
          </view>
          <view class="info-item">
            <view class="info-icon-wrap">
              <text>👤</text>
            </view>
            <text class="info-text">{{ selectedCourse.teacher }}</text>
          </view>
          <view class="info-item">
            <view class="info-icon-wrap">
              <text>🕐</text>
            </view>
            <text class="info-text">{{ selectedCourse.time }}</text>
          </view>
          <view class="info-item">
            <view class="info-icon-wrap">
              <text>📅</text>
            </view>
            <text class="info-text">{{ selectedCourse.weeks }}</text>
          </view>
        </view>
        <view class="modal-close tap-scale" @tap="selectedCourse = null">
          <text class="close-text">关闭</text>
        </view>
      </view>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

const currentWeek = ref(8)
const selectedCourse = ref<any>(null)

const todayIndex = computed(() => new Date().getDay() - 1)

const weekdays = computed(() => {
  const days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
  const now = new Date()
  const monday = new Date(now)
  monday.setDate(now.getDate() - now.getDay() + 1)
  return days.map((label, i) => {
    const d = new Date(monday)
    d.setDate(monday.getDate() + i + (currentWeek.value - 1) * 7)
    return { label, date: `${d.getMonth() + 1}/${d.getDate()}` }
  })
})

const timeSlots = [
  { period: 1, time: '08:00' },
  { period: 2, time: '09:40' },
  { period: 3, time: '10:00' },
  { period: 4, time: '11:40' },
  { period: 5, time: '14:00' },
  { period: 6, time: '15:40' },
  { period: 7, time: '16:00' },
  { period: 8, time: '17:40' },
  { period: 9, time: '19:00' },
  { period: 10, time: '20:40' },
]

interface Course {
  name: string
  room: string
  teacher: string
  time: string
  weeks: string
  color: string
  day: string
  period: number
}

const courses: Course[] = [
  { name: '高等数学', room: 'A301', teacher: '张教授', time: '08:00-09:40', weeks: '1-16周', color: 'rgba(99,102,241,0.12)', day: '周一', period: 1 },
  { name: '大学英语', room: 'B205', teacher: '李老师', time: '10:00-11:40', weeks: '1-16周', color: 'rgba(139,92,246,0.12)', day: '周二', period: 3 },
  { name: '数据结构', room: 'C102', teacher: '王教授', time: '14:00-15:40', weeks: '1-18周', color: 'rgba(16,185,129,0.12)', day: '周三', period: 5 },
  { name: '线性代数', room: 'A205', teacher: '赵教授', time: '08:00-09:40', weeks: '2-17周', color: 'rgba(244,63,94,0.12)', day: '周四', period: 1 },
  { name: '体育', room: '体育馆', teacher: '陈老师', time: '14:00-15:40', weeks: '1-16周', color: 'rgba(245,158,11,0.12)', day: '周五', period: 5 },
  { name: '大学物理', room: 'D401', teacher: '刘教授', time: '10:00-11:40', weeks: '1-18周', color: 'rgba(99,102,241,0.12)', day: '周一', period: 3 },
  { name: '数据结构', room: 'C102', teacher: '王教授', time: '14:00-15:40', weeks: '1-18周', color: 'rgba(16,185,129,0.12)', day: '周五', period: 3 },
]

function getCourse(day: string, period: number): Course | null {
  return courses.find(c => c.day === day && c.period === period) || null
}

function changeWeek(delta: number) {
  currentWeek.value = Math.max(1, currentWeek.value + delta)
}

function showDetail(course: Course | null) {
  if (course) selectedCourse.value = course
}
</script>

<style scoped>
.schedule-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: var(--bg);
}

.header {
  padding: calc(var(--status-bar-height, 44px) + 24rpx) 32rpx 36rpx;
}

.header-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 1;
}

.header-title {
  font-size: 40rpx;
  font-weight: 700;
  color: #fff;
}

.week-selector {
  display: flex;
  align-items: center;
  gap: 20rpx;
}

.week-arrow {
  width: 56rpx;
  height: 56rpx;
  border-radius: 50%;
  background: rgba(255,255,255,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
}

.arrow-text {
  font-size: 36rpx;
  color: #fff;
  font-weight: 600;
}

.week-text {
  font-size: 28rpx;
  color: #fff;
  font-weight: 700;
  min-width: 120rpx;
  text-align: center;
}

.weekdays {
  display: grid;
  grid-template-columns: 80rpx repeat(7, 1fr);
  background: var(--card);
  border-bottom: 1rpx solid var(--border);
  padding-bottom: 8rpx;
}

.weekday {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 16rpx 0;
  gap: 8rpx;
}

.weekday-label {
  font-size: 22rpx;
  color: var(--text-muted);
  font-weight: 500;
}

.weekday.active .weekday-label {
  color: var(--primary);
  font-weight: 700;
}

.weekday-date-wrap {
  width: 44rpx;
  height: 44rpx;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.weekday-date-wrap.active {
  background: var(--primary);
}

.weekday-date {
  font-size: 20rpx;
  color: var(--text-muted);
  font-weight: 500;
}

.weekday.active .weekday-date {
  color: #fff;
  font-weight: 700;
}

.timetable {
  flex: 1;
  padding: 0 8rpx;
}

.time-grid { padding-top: 8rpx; }

.time-row {
  display: flex;
  align-items: stretch;
  height: 120rpx;
}

.time-label {
  width: 80rpx;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 0 4rpx;
}

.period-text {
  font-size: 18rpx;
  color: var(--text-muted);
}

.time-text {
  font-size: 16rpx;
  color: var(--text-muted);
  margin-top: 2rpx;
}

.course-columns {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  flex: 1;
}

.course-cell {
  padding: 4rpx;
  height: 100%;
  box-sizing: border-box;
  border: 1rpx solid var(--border);
}

.course-block {
  width: 100%;
  height: 100%;
  border-radius: 10rpx;
  padding: 6rpx;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  border-left: 4rpx solid var(--primary);
}

.course-name {
  font-size: 18rpx;
  font-weight: 700;
  color: var(--text);
}

.course-room {
  font-size: 14rpx;
  color: var(--text-muted);
  margin-top: 4rpx;
}

/* 弹窗 */
.modal-mask {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
  animation: fadeIn 0.2s ease;
}

.modal-content {
  width: 600rpx;
  padding: 0;
  overflow: hidden;
  animation: slideUp 0.3s ease-out;
}

.modal-header {
  padding: 36rpx 36rpx 0;
}

.modal-title {
  font-size: 36rpx;
  font-weight: 800;
  display: block;
}

.modal-body {
  padding: 28rpx 36rpx;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 16rpx;
  margin-bottom: 20rpx;
}

.info-icon-wrap {
  width: 48rpx;
  height: 48rpx;
  border-radius: 12rpx;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24rpx;
  flex-shrink: 0;
}

.info-text {
  font-size: 28rpx;
  color: var(--text-secondary);
}

.modal-close {
  margin: 0 36rpx 36rpx;
  text-align: center;
  padding: 24rpx;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  border-radius: 16rpx;
}

.close-text {
  color: #fff;
  font-size: 28rpx;
  font-weight: 700;
}
</style>
