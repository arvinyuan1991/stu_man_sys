from django.db import models

# Create your models here.
from classes.models import Class
from subject.models import Subject
from teachers.models import Teacher


# 课程类
class Courses(models.Model):
    """课程类"""
    start_time = models.DateTimeField(verbose_name="上课时间")
    end_time = models.DateTimeField(verbose_name="下课时间")
    total_time = models.IntegerField(verbose_name="总时长")
    classes = models.ForeignKey(Class, on_delete=models.PROTECT, verbose_name="班级")
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name='教师')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='学科')
    title = models.CharField(max_length=60, verbose_name='标题')
    class_room = models.IntegerField(verbose_name='教室')
    student_money = models.IntegerField(verbose_name='学生课时费用')
    teacher_money = models.IntegerField(verbose_name='教师课时费用')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tb_cour"
        verbose_name = "课程"
        verbose_name_plural = verbose_name
