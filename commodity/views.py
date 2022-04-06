from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import F
from .models import *


def commodityView(request):
    """商品列表页视图函数"""

    title = "商品列表"
    classContent = "commoditys  "

    # 根据模型CommodityType去查询相应信息
    firsts = CommodityType.objects.values("firsts").distinct()
    typesList  = CommodityType.objects.all()

    # 获取get请求参数
    t = request.GET.get("t", "")  # 分页的商品信息
    s = request.GET.get("s", "sold")  # 商品排序方式，未给出默认销量sola
    p = request.GET.get("p", 1)  # 页数
    n = request.GET.get("n", "")  # 商品搜索

    # 先拿出全部商品数据
    commodity_info = CommodityInfo.objects.all()

    # 分类筛选
    if t:
        types = CommodityType.objects.filter(id=t).first()
        commodity_info = commodity_info.filter(types=types.seconds)

    # 排序筛选
    if s:
        commodity_info = commodity_info.order_by("-" + s)

    # 模糊筛选
    if t:
        commodity_info = commodity_info.filter(name_contains=n)

    # 分页功能
    paginator = Paginator(commodity_info, 6)

    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, "commodity.html", locals())


def detailView(request, id):
    """商品详细页视图函数"""

    title = "商品介绍"
    classContent  = "details"
    commoditys = CommodityInfo.objects.filter(id=id).first()
    items = CommodityInfo.objects.exclude(id=id).order_by("-sold")[:5]
    likesList = request.session.get("likes", [])
    likes = True if id in likesList else False
    return render(request, "details.html", locals())


def collectView(request):
    """收藏视图函数"""

    id = request.GET.get("id", "")
    result = {"result": "已收藏"}
    likes = request.session.get("likes", [])

    if id and not int(id) in likes:
        CommodityInfo.objects.filter(id=id).update(likes=F("likes") + 1)
        result["result"] = "收藏成功"
        request.session["likes"] = likes + [int(id)]

    return JsonResponse(result)
