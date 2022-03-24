import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "babys.settings")  # babys 项目名称
django.setup()

from commodity.models import CommodityType
from django.db.models import F, Q

# 删除全部数据
c = CommodityType.objects.all().delete()

# 删除指定数据
c = CommodityType.objects.get(id=1).delete()

# 删除多条数据
c = CommodityType.objects.filter(firsts="中国人").delete()
