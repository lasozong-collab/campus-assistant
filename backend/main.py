"""
校园助手后端 — FastAPI
本地可直接运行，无需外部 API Key
启动方式：python main.py
"""

import os
import sys
from pathlib import Path

# 确保项目根目录在 path 中
sys.path.insert(0, str(Path(__file__).parent))

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import chat, schedule, market, articles, profile

app = FastAPI(title="校园助手 API", version="1.0.0")

# 跨域配置（允许前端访问）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(chat.router, prefix="/api/chat", tags=["聊天"])
app.include_router(schedule.router, prefix="/api/schedule", tags=["课表"])
app.include_router(market.router, prefix="/api/market", tags=["集市"])
app.include_router(articles.router, prefix="/api/articles", tags=["发现"])
app.include_router(profile.router, prefix="/api/profile", tags=["个人"])


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "校园助手后端运行中"}


if __name__ == "__main__":
    print("=" * 50)
    print("  校园助手后端启动中...")
    print("  API 文档：http://localhost:8000/docs")
    print("=" * 50)
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
