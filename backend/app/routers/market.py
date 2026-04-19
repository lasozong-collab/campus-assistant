"""
集市路由 — 二手交易 / 失物招领 / 代取快递
"""

from fastapi import APIRouter, Query
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# ---------- 模拟数据 ----------

ITEMS = [
    {"id": 1, "avatar": "👩", "author": "小美", "time": "10分钟前", "category": "二手交易", "title": "九成新iPad Air5", "desc": "去年买的，贴膜保护完好，128G蓝色，因换新机出", "price": "2800元", "likes": 23, "comments": 8},
    {"id": 2, "avatar": "👦", "author": "阿强", "time": "30分钟前", "category": "失物招领", "title": "捡到一张校园卡", "desc": "在图书馆三楼捡到的，姓名看起来是'王同学'，请联系认领", "price": None, "likes": 5, "comments": 2},
    {"id": 3, "avatar": "👧", "author": "学霸姐", "time": "1小时前", "category": "二手交易", "title": "考研全套资料打包出", "desc": "包含数学一、英语一、政治全套教材和真题，附赠笔记", "price": "80元", "likes": 45, "comments": 19},
    {"id": 4, "avatar": "🧑", "author": "快递达人", "time": "2小时前", "category": "代取快递", "title": "代取菜鸟驿站快递", "desc": "长期代取，5元/件，当天下单当天送达，校内免配送费", "price": "5元/件", "likes": 12, "comments": 6},
    {"id": 5, "avatar": "👩", "author": "小姐姐", "time": "3小时前", "category": "二手交易", "title": "全新Nike运动鞋", "desc": "买小了一码穿不了，42码，全新带吊牌", "price": "350元", "likes": 31, "comments": 14},
    {"id": 6, "avatar": "👦", "author": "理工男", "time": "4小时前", "category": "失物招领", "title": "在食堂丢了一个水杯", "desc": "蓝色保温杯，上面有贴纸，有看到的同学请私信，必有重谢！", "price": None, "likes": 3, "comments": 1},
    {"id": 7, "avatar": "🧑", "author": "跑腿小哥", "time": "5小时前", "category": "代取快递", "title": "代购代拿服务", "desc": "可以代买奶茶、零食、日用品，校内配送15分钟达", "price": "3元起", "likes": 8, "comments": 3},
    {"id": 8, "avatar": "👧", "author": "学姐", "time": "6小时前", "category": "二手交易", "title": "专业课本低价转让", "desc": "计算机专业大三全部课本，每本20元，全套打包100", "price": "20元/本", "likes": 56, "comments": 22},
]


class NewItem(BaseModel):
    category: str
    title: str
    desc: str
    price: str | None = None
    author: str = "匿名用户"


@router.get("/list")
async def get_items(category: str = Query(default="全部")):
    """获取集市列表"""
    if category == "全部":
        return {"items": ITEMS}
    return {"items": [i for i in ITEMS if i["category"] == category]}


@router.get("/item/{item_id}")
async def get_item(item_id: int):
    """获取单个商品详情"""
    for item in ITEMS:
        if item["id"] == item_id:
            return item
    return {"error": "未找到该商品"}


@router.post("/publish")
async def publish_item(item: NewItem):
    """发布新商品"""
    new_id = max(i["id"] for i in ITEMS) + 1
    avatars = ["🧑", "👩", "👦", "👧"]
    new_item = {
        "id": new_id,
        "avatar": "🧑",
        "author": item.author,
        "time": "刚刚",
        "category": item.category,
        "title": item.title,
        "desc": item.desc,
        "price": item.price,
        "likes": 0,
        "comments": 0,
    }
    ITEMS.insert(0, new_item)
    return {"message": "发布成功", "item": new_item}


@router.post("/like/{item_id}")
async def like_item(item_id: int):
    """点赞"""
    for item in ITEMS:
        if item["id"] == item_id:
            item["likes"] += 1
            return {"message": "点赞成功", "likes": item["likes"]}
    return {"error": "未找到该商品"}
