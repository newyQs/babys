import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "babys.settings")  # babys 项目名称
django.setup()

from commodity.models import CommodityType
from django.db.models import F, Q

# 直接增加数据

# c = CommodityType()
# c.firsts = "安徽"
# c.seconds = "合肥"
# c.save()

# c = CommodityType(firsts="浙江", seconds="杭州")
# c.save()

# d = dict(firsts="江苏", seconds="南京")
# c = CommodityType(**d)
# c.save()

# create(self, **kwargs)
# c = CommodityType.objects.create(firsts="广东", seconds="广州")

# d = dict(firsts="江西", seconds="南昌")
# c = CommodityType.objects.create(**d)

# get_or_creat()
# get_or_create(self, defaults=None, **kwargs)
# c = CommodityType.objects.get_or_create(firsts="福建", seconds="福州")

# update_or_creat()
# update_or_create(self, defaults=None, **kwargs)
c = CommodityType.objects.update_or_create(firsts="云南", seconds="昆明")

# django的添加操作建议如下操作:
"""
# 直接使用create操作，但不会去重
c=CommodityType.objects.create(field1=value1, field2=value2, ...)

# 使用get_or_create()

# 使用update_or_create()
"""
