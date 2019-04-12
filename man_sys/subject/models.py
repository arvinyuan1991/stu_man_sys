from django.db import models


# Create your models here.


# 学科模型类
class Subject(models.Model):
    """学科模型类"""
    name = models.CharField(max_length=40, verbose_name='名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_sub"
        verbose_name = "学科"
        verbose_name_plural = verbose_name
