"""
ORM操作数据示例
['aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter',
'contains', 'contribute_to_class', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager',
'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter',
'first', 'from_queryset', 'get', 'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator', 'last',
'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update',
'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list']
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "babys.settings")  # babys 项目名称
django.setup()

from commodity.models import CommodityType
from django.db.models import F, Q

# (1) 添加数据
# # 方法一
# t = CommodityType()
# t.firsts = "童装"
# t.seconds = "女装"
# t.save()
#
# # 方法二
# t = CommodityType(firsts="儿童早教", seconds="童话故事")
# t.save()
#
# # 方法三(建议)
# t = CommodityType.objects.create(firsts="儿童用品", seconds="婴儿车")
#
# # 方法四
# d = dict(firsts="奶粉辅食", seconds="磨牙饼干")
# t = CommodityType.objects.create(**d)

# (2) get_or_create()
# 存在就忽略，不存在就创建
# d = dict(firsts="奶粉辅食", seconds="营养品")
# t = CommodityType.objects.get_or_create(**d)
#
# print(t)  # (<CommodityType: 11>, False) # 创建成功，即为True
# print(t[0].id)
#
# # (3) update_or_create()
# # 存在就更新，不存在就创建
# d = dict(firsts="儿童早教", seconds="儿童玩具")
# t = CommodityType.objects.update_or_create(**d)
#
# print(t)  # (<CommodityType: 11>, False) # 更新成功，即为True
# print(t[0].id)

# (4) 更新数据
# t = CommodityType.objects.get(id=1)
# print(t.firsts)
# t.firsts = "儿童用品"
# print(t.firsts)

# t = CommodityType.objects.filter(id=1).update(seconds="男装")
# t = CommodityType.objects.filter(id=1).update(seconds="童鞋")

# 不使用查询，默认对全表进行更新
# CommodityType.objects.update(firsts="母婴用品")

# 使用内置的F方法实现数据的自增和自减
# t = CommodityType.objects.filter(id=1)
# t.update(id=F('id') + 10)

# (5) 批量更新
# t1 = CommodityType.objects.create(firsts="奶粉辅食", seconds="纸尿片")
# t2 = CommodityType.objects.create(firsts="儿童用品", seconds="进口奶粉")
#
# t1.firsts = "儿童用品"
# t2.seconds = "婴儿车"
# CommodityType.objects.bulk_update([t1, t2], fields=['firsts', 'seconds'])

# (6) 删除数据

# 删除表中全部数据
# CommodityType.objects.all().delete()

# 删除一条id=1的数据
# CommodityType.objects.get(id=1).delete()

# 删除多条数据
# CommodityType.objects.filter(firsts="儿童用品").delete()

t = CommodityType.objects
print(dir(t))


