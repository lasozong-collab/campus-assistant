"""
发现页路由 — 校园攻略文章
"""

from fastapi import APIRouter, Query

router = APIRouter()

# ---------- 模拟数据 ----------

ARTICLES = [
    {"id": 1, "title": "大一新生选课全攻略", "summary": "手把手教你如何选课，避开坑课，选到心仪的老师", "emoji": "📚", "coverColor": "linear-gradient(135deg, #667eea, #764ba2)", "tag": "学习", "author": "学长说", "views": "2.3万", "content": "选课是大学生活的第一道关卡。本文从选课流程、课程类型、避坑技巧三个维度，帮你一次性搞定选课难题。\n\n一、选课三轮制\n金陵科技学院选课分为三轮：预选（抽签制）→ 补选（抽签制）→ 抢选（先到先得）。\n\n二、选课建议\n• 公选课建议大一就开始修，分散压力\n• 关注课程考核方式（考试/论文/汇报）\n• 多向学长学姐打听老师给分情况\n\n三、避坑指南\n• 不要把课全排到同一天\n• 注意上课校区和教室距离\n• 退课要在规定时间内操作"},
    {"id": 2, "title": "校园周边美食地图", "summary": "东门到西门，最值得吃的20家店全在这", "emoji": "🍜", "coverColor": "linear-gradient(135deg, #f093fb, #f5576c)", "tag": "美食", "author": "吃货小分队", "views": "1.8万", "content": "江宁大学城周边美食合集！\n\n🌟 必吃榜\n1. 东门烤肉饭 — 人均15元\n2. 北门麻辣烫 — 人均12元\n3. 南区炸鸡 — 人均18元\n4. 大学城步行街小龙虾 — 人均50元\n\n💡 省钱技巧\n• 学校食堂人均8-15元\n• 外卖拼单更划算\n• 关注商家学生优惠"},
    {"id": 3, "title": "社团招新指南2025", "summary": "30+社团详细介绍，找到最适合你的组织", "emoji": "🎭", "coverColor": "linear-gradient(135deg, #4facfe, #00f2fe)", "tag": "活动", "author": "学生会", "views": "3.1万", "content": "10月初百团大战，社团招新季来啦！\n\n🔥 热门社团\n• 计算机协会 — 程序员的快乐老家\n• 摄影社 — 记录校园每一刻\n• 篮球社 — 挥洒汗水的地方\n• 辩论社 — 锻炼口才和思维\n• 志愿者协会 — 奉献爱心的平台\n\n💡 建议：大一大二多参加，但别贪多，2-3个就够了"},
    {"id": 4, "title": "图书馆生存手册", "summary": "预约技巧、最佳座位、充电位置全部公开", "emoji": "📖", "coverColor": "linear-gradient(135deg, #43e97b, #38f9d7)", "tag": "学习", "author": "学霸联盟", "views": "1.5万", "content": "图书馆是大学最重要的学习场所之一。\n\n📍 基本信息\n• 开放时间：7:30-22:00（考试周延长）\n• 凭校园卡刷卡进入\n• 借书上限：10本，期限30天\n\n💡 实用技巧\n• 考试周早上7点去排队占座\n• 三楼靠窗座位视野最好\n• 自习区有充电插座\n• 二楼有打印复印服务"},
    {"id": 5, "title": "宿舍好物推荐清单", "summary": "提升宿舍生活品质的30件神器", "emoji": "🏠", "coverColor": "linear-gradient(135deg, #fa709a, #fee140)", "tag": "生活", "author": "生活达人", "views": "2.7万", "content": "宿舍好物推荐TOP 10！\n\n1. 床上书桌 — 方便在床上学习\n2. 台灯 — 护眼必备\n3. 收纳盒 — 整理桌面神器\n4. 遮光帘 — 保证睡眠质量\n5. 小风扇 — 夏天续命\n6. 桌面收纳架 — 空间翻倍\n7. 眼罩+耳塞 — 室友作息不同必备\n8. 多孔排插 — 满足充电需求\n9. 挂式垃圾桶 — 节省地面空间\n10. 懒人支架 — 看剧吃饭两不误"},
    {"id": 6, "title": "奖学金申请全流程", "summary": "国奖、校奖、企业奖，一篇搞懂申请流程", "emoji": "🏆", "coverColor": "linear-gradient(135deg, #a18cd1, #fbc2eb)", "tag": "学习", "author": "资助中心", "views": "4.2万", "content": "奖学金全攻略！\n\n💰 国家奖学金\n金额：8000元/年\n条件：成绩排名前5%，综合素质突出\n\n💰 国家励志奖学金\n金额：5000元/年\n条件：家庭经济困难 + 成绩优秀\n\n💰 校优秀学生奖学金\n金额：500-3000元\n条件：成绩排名前30%\n\n📅 申请时间\n每年9-10月，关注学校通知"},
    {"id": 7, "title": "校运动会报名指南", "summary": "项目介绍、报名方式、训练计划一应俱全", "emoji": "🏃", "coverColor": "linear-gradient(135deg, #ffecd2, #fcb69f)", "tag": "活动", "author": "体育部", "views": "8600", "content": "校运动会报名全攻略！\n\n🏃 个人项目\n100m/200m/400m/800m/1500m/跳远/跳高/铅球\n\n🤝 集体项目\n4×100m接力/拔河/多人跳绳\n\n📅 报名方式\n通过班级体委或体育部报名，一般在运动会前2周截止"},
    {"id": 8, "title": "食堂窗口评分排行", "summary": "全校6个食堂最火窗口TOP20", "emoji": "🍽️", "coverColor": "linear-gradient(135deg, #89f7fe, #66a6ff)", "tag": "美食", "author": "美食团", "views": "3.5万", "content": "食堂窗口红黑榜！\n\n🏆 TOP 5 窗口\n1. 北区二楼 — 黄焖鸡米饭（永远的神）\n2. 东区一楼 — 酸菜鱼\n3. 南区三楼 — 石锅拌饭\n4. 北区一楼 — 麻辣香锅\n5. 东区二楼 — 瓦罐汤\n\n⚠️ 避雷区\n（此处省略，留给你自己去发现）"},
]


@router.get("/list")
async def get_articles(tag: str = Query(default="全部")):
    """获取文章列表"""
    if tag == "全部":
        result = ARTICLES
    else:
        result = [a for a in ARTICLES if a["tag"] == tag]
    # 返回列表时不包含完整内容
    return {"articles": [{"id": a["id"], "title": a["title"], "summary": a["summary"],
                         "emoji": a["emoji"], "coverColor": a["coverColor"],
                         "tag": a["tag"], "author": a["author"], "views": a["views"]}
                        for a in result]}


@router.get("/detail/{article_id}")
async def get_article(article_id: int):
    """获取文章详情"""
    for article in ARTICLES:
        if article["id"] == article_id:
            return article
    return {"error": "文章未找到"}


@router.get("/search")
async def search_articles(keyword: str = Query(default="")):
    """搜索文章"""
    if not keyword:
        return {"articles": []}
    results = [a for a in ARTICLES if keyword in a["title"] or keyword in a["summary"] or keyword in a["tag"]]
    return {"articles": results, "count": len(results)}
