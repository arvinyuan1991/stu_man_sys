from django.db import models

# Create your models here.

from students.models import Student
from subject.models import Subject


# 成绩模型类
class Results(models.Model):
    """成绩模型类"""
    point = models.IntegerField(verbose_name='分数')
    time = models.DateField(verbose_name='考试时间')
    name = models.CharField(max_length=40, verbose_name='名称')
    student = models.ForeignKey(Student, on_delete=models.PROTECT, verbose_name='学生')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='学科')
    comment = models.CharField(max_length=80, verbose_name='评价')

    def __str__(self):
        return self.name

    class meta:
        db_table = 'tb_res'
        verbose_name = '成绩'
        verbose_name_plural = verbose_name
