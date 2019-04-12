from django.db import models


# Create your models here.
# 教师模型类
class Teacher(models.Model):
    """教师模型类"""
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    GENDER_CHOICES = (
        (0, '男'), (1, '女')
    )
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    total_hour = models.IntegerField(verbose_name='总课时')
    total_money = models.IntegerField(verbose_name='总费用')
    comment = models.CharField(max_length=80, verbose_name='简介')

    def __str__(self):
        return self.name

    class meta:
        db_table = 'tb_tea'
        verbose_name = '教师'
        verbose_name_plural = verbose_name
