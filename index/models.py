from django.db import models


# Create your models here.
class PersonInfo(models.Model):
    """个人信息表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hireDate = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_person_info"
        verbose_name = "人员信息"


class VocationInfo(models.Model):
    """职业信息表"""
    id = models.AutoField(primary_key=True)
    job = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    payment = models.IntegerField(null=True, blank=True)
    name = models.ForeignKey(PersonInfo, on_delete=models.CASCADE, related_name="ps")

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "tb_vocation_info"
        verbose_name = "职业信息"


class Province(models.Model):
    """省份信息表"""
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "tb_province"


class City(models.Model):
    """城市信息表"""
    name = models.CharField(max_length=5)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "tb_city"


class Person(models.Model):
    """人物信息表"""
    name = models.CharField(max_length=10)
    living = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "tb_person"


class Performer(models.Model):
    """人员信息表"""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "tb_performer"


class Program(models.Model):
    """节目信息表"""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    performer = models.ManyToManyField(Performer)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "tb_program"
