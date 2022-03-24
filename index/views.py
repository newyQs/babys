from django.shortcuts import render
from commodity.models import *
from django.views.generic.base import TemplateView


def indexView(request):
    # title = '首页'
    # class_content = ''
    # commodity_info = CommodityInfo.objects.order_by('-sold').all()[:8]
    types = CommodityType.objects.all()

    cl = [x.seconds for x in types if x.firsts == "儿童服饰"]
    clothes = CommodityInfo.objects.filter(types__in=cl).order_by('-sold')[:5]

    fl = [x.seconds for x in types if x.firsts == "奶粉辅食"]
    foods = CommodityInfo.objects.filter(types__in=fl).order_by('-sold')[:5]

    gl = [x.seconds for x in types if x.firsts == "儿童用品"]
    goods = CommodityInfo.objects.filter(types__in=gl).order_by("-sold")[:5]

    return render(request, 'index.html', locals())


class indexClassView(TemplateView):
    template_name = 'index.html'
    template_engine = None
    content_type = None
    extra_context = {"title": "首页", "class_content": ""}

    def get_context_data(self, **kwargs):
        context = super(indexClassView, self).get_context_data(**kwargs)
        context["commodity_info"] = CommodityInfo.objects.order_by('-sold').all()[:8]
        types = CommodityType.objects.all()

        cl = [x.seconds for x in types if x.firsts == "儿童服饰"]
        context["clothes"] = CommodityInfo.objects.filter(types__in=cl).order_by('-sold')[:5]

        fl = [x.seconds for x in types if x.firsts == "奶粉辅食"]
        context["foods "] = CommodityInfo.objects.filter(types__in=fl).order_by('-sold')[:5]

        gl = [x.seconds for x in types if x.firsts == "儿童用品"]
        context["goods"] = CommodityInfo.objects.filter(types__in=gl).order_by("-sold")[:5]

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
