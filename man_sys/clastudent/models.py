from django.db import models

# Create your models here.
from classes.models import Class
from students.models import Student


# 班级学生模型类
class ClassStudent(models.Model):
    """班级学生模型类"""
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='班级')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')

    def __str__(self):
        return self.classes.name

    class meta:
        db_table = 'tb_cst'
        verbose_name = '班级学生'
        verbose_name_plural = verbose_name
