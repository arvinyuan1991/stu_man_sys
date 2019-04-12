from django.db import models

# Create your models here.
from courses.models import Courses
from teachers.models import Teacher


# 教师缺勤模型类
class TeacherAbsences(models.Model):
    """教师缺勤模型类"""
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='课程')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='教师')

    class meta:
        db_table = 'tb_tab'
        verbose_name = '教师缺勤'
        verbose_name_plural = verbose_name
