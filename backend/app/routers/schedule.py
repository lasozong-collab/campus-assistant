"""
课表路由
"""

from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()

# ---------- 模拟数据 ----------

COURSES = [
    {"name": "高等数学", "room": "A301", "teacher": "张教授", "time": "08:00-09:40", "weeks": "1-16周", "color": "#4F6EF7", "day": "周一", "period": 1},
    {"name": "大学物理", "room": "D401", "teacher": "刘教授", "time": "10:00-11:40", "weeks": "1-18周", "color": "#00C9A7", "day": "周一", "period": 3},
    {"name": "大学英语", "room": "B205", "teacher": "李老师", "time": "10:00-11:40", "weeks": "1-16周", "color": "#7C5CFC", "day": "周二", "period": 3},
    {"name": "思想政治", "room": "A101", "teacher": "王老师", "time": "14:00-15:40", "weeks": "1-18周", "color": "#FF6B6B", "day": "周二", "period": 5},
    {"name": "数据结构", "room": "C102", "teacher": "王教授", "time": "14:00-15:40", "weeks": "1-18周", "color": "#00C9A7", "day": "周三", "period": 5},
    {"name": "线性代数", "room": "A205", "teacher": "赵教授", "time": "08:00-09:40", "weeks": "2-17周", "color": "#FF6B6B", "day": "周四", "period": 1},
    {"name": "Python程序设计", "room": "C201", "teacher": "孙老师", "time": "10:00-11:40", "weeks": "1-16周", "color": "#FFB74D", "day": "周四", "period": 3},
    {"name": "体育", "room": "体育馆", "teacher": "陈老师", "time": "14:00-15:40", "weeks": "1-16周", "color": "#FFB74D", "day": "周五", "period": 5},
    {"name": "数据结构", "room": "C102", "teacher": "王教授", "time": "14:00-15:40", "weeks": "1-18周", "color": "#00C9A7", "day": "周五", "period": 3},
]

TIME_SLOTS = [
    {"period": 1, "time": "08:00"},
    {"period": 2, "time": "09:40"},
    {"period": 3, "time": "10:00"},
    {"period": 4, "time": "11:40"},
    {"period": 5, "time": "14:00"},
    {"period": 6, "time": "15:40"},
    {"period": 7, "time": "16:00"},
    {"period": 8, "time": "17:40"},
    {"period": 9, "time": "19:00"},
    {"period": 10, "time": "20:40"},
]


@router.get("/courses")
async def get_courses(week: int = Query(default=8)):
    """获取某周全部课程"""
    # 根据周次过滤（模拟）
    valid_courses = []
    for c in COURSES:
        weeks_str = c["weeks"]
        try:
            start, end = weeks_str.replace("周", "").split("-")
            start, end = int(start), int(end)
            if start <= week <= end:
                valid_courses.append(c)
        except (ValueError, AttributeError):
            valid_courses.append(c)
    return {"week": week, "courses": valid_courses}


@router.get("/today")
async def get_today_courses():
    """获取今日课程"""
    days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    today = days[min(max(0, __import__("datetime").datetime.now().weekday()), 6)]
    today_courses = [c for c in COURSES if c["day"] == today]

    # 标记进行中的课程
    from datetime import datetime
    now_hour = datetime.now().hour
    for c in today_courses:
        start_h = int(c["time"].split(":")[0])
        c["active"] = now_hour >= start_h and now_hour < start_h + 2

    return {"day": today, "courses": today_courses}


@router.get("/time-slots")
async def get_time_slots():
    """获取时间节次"""
    return {"slots": TIME_SLOTS}
