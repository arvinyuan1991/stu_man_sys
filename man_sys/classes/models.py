from django.db import models

# Create your models here.
from students.models import Student


# 班级模型类
class Class(models.Model):
    """班级模型类"""
    name = models.CharField(max_length=40, verbose_name='班级名')

    def __str__(self):
        return self.name

    class meta:
        db_table = 'tb_class'
        verbose_name = '班级'
        verbose_name_plural = verbose_name
