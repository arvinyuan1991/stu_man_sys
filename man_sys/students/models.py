from django.db import models


# Create your models here.

# 学生模型类
class Student(models.Model):
    """学生模型类"""
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    GENDER_CHOICES = (
        (0, '男'), (1, '女')
    )
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    total_money = models.IntegerField(verbose_name='充值金额')
    remain_money = models.IntegerField(verbose_name='剩余金额')
    total_hour = models.IntegerField(verbose_name='总课时')
    use_hour = models.IntegerField(verbose_name='已上课时')
    remain_hour = models.IntegerField(verbose_name='剩余课时')

    def __str__(self):
        return self.name

    class meta:
        db_table = 'tb_stu'
        verbose_name = '学生'
        verbose_name_plural = verbose_name
