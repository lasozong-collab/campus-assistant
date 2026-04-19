"""
个人中心路由
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# ---------- 模拟用户数据 ----------

USER_PROFILE = {
    "name": "Flechazo",
    "student_id": "2023001XXXX",
    "department": "计算机科学与技术",
    "grade": "2023级",
    "avatar": "🧑‍🎓",
    "stats": {
        "favorites": 12,
        "published": 5,
        "likes_received": 28,
    },
    "gpa": 3.62,
    "credits_total": 68.5,
    "credits_required": 160,
}


class FeedbackRequest(BaseModel):
    content: str
    contact: str = ""


@router.get("/info")
async def get_profile():
    """获取用户信息"""
    return USER_PROFILE


@router.get("/stats")
async def get_stats():
    """获取用户统计"""
    return USER_PROFILE["stats"]


@router.get("/gpa")
async def get_gpa():
    """获取 GPA 和学分信息"""
    return {
        "gpa": USER_PROFILE["gpa"],
        "credits_total": USER_PROFILE["credits_total"],
        "credits_required": USER_PROFILE["credits_required"],
        "progress": round(USER_PROFILE["credits_total"] / USER_PROFILE["credits_required"] * 100, 1),
    }


@router.post("/feedback")
async def submit_feedback(req: FeedbackRequest):
    """提交意见反馈"""
    return {"message": "感谢你的反馈！我们会尽快处理～", "content": req.content}
