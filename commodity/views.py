from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import F
from .models import *


def commodityView(request):
    title = "商品列表"
    class_count = "commoditys"

    # 根据CommodityType去查询相应信息
    firsts = CommodityType.objects.values("firsts").distinct()
    type_list = CommodityType.objects.all()

    # 获取请求参数：GET请求
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


def collectView(request):
    mid = request.GET.get("id", "")
    result = {"result": "已收藏"}
    likes = request.session.get("likes", [])

    if mid and not int(mid) in likes:
        CommodityInfo.objects.filter(id=mid).update(likes=F("likes") + 1)
        result["result"] = "收藏成功"
        request.session["likes"] = likes + [int(mid)]

    return JsonResponse(result)
