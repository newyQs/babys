from django.db import models


# Create your models here.
class PersonInfo(models.Model):
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
