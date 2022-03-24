import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "babys.settings")  # babys 项目名称
django.setup()

from commodity.models import CommodityType
from django.db.models import F, Q

"""
.all()

.get()
.get_or_create()
.bulk_create()

.update()
.update_or_create()
.bulk_update()

.filter()
.delete()

.exists()

.difference()
.union()
.intersection()

.count()
.reverse()

.values()
.values_list()

.aggregate()
.alias()
.annotate()
.check()
.complex_filter()

.contains()

.order_by()
"""
c = CommodityType.objects
