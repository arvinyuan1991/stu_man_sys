from django.db import models

# Create your models here.
from courses.models import Courses
from students.models import Student


# 学生缺勤类
class StudentAbsences(models.Model):
    """学生缺勤类"""
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='课程')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')

    class meta:
        db_table = 'tb_sab'
        verbose_name = '学生缺勤'
        verbose_name_plural = verbose_name
