import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "babys.settings")  # babys 项目名称
django.setup()

from commodity.models import CommodityType
from django.db.models import F, Q

# update(self, **kwargs)
# 直接使用update()则是全局更新
# c = CommodityType.objects.update(firsts="中国")
# 或这样写
# c = CommodityType.objects.all().update(firsts="中国")

# 适合修改一条数据，如修改 id=1 字段 first=中国人
# c = CommodityType.objects.get(id=1)
# c.firsts = "中国人"
# c.save()

# 适合修改多条数据
c = CommodityType.objects.filter(id=2).update(firsts="中国人")

# 注意get和filter的区别：
"""
get查询的值必须存在，且只有一条记录，否则报错
filter查询的值无序存在，可以有多条记录，不会报错
"""

# django的更新建议如下:
"""
# 更新id=mid的数据（这里的id是主键，所有只会更新一条数据），熟悉设置为：field1=value1, field2=value2, ...
c = CommodityType.objects.filter(id=mid).update(field1=value1, field2=value2, ...)
# filter使用其他字段
c = CommodityType.objects.filter(fieldN=valueN).update(field1=value1, field2=value2, ...)

# get筛选更新
c = CommodityType.objects.get(id=mid)
c.field1=value1
c.field2=value2
c.save()

# 不加筛选条件，直接更新全部
c = CommodityType.objects.update(field1=value1, field2=value2, ...)
"""
