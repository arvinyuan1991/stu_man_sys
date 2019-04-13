import xadmin

# Register your models here.
from absteachers import models
from courses.models import Courses
from teachers.models import Teacher


class TeacherAbsencesAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['id', 'teacher', 'course']
    list_per_page = 5
    ordering = ['id']

    # 重写save_models根据缺勤更新学生的课时和课时费
    def save_model(self):
        """重写save_models根据缺勤更新学生的课时和课时费"""
        obj = self.new_obj
        teacher_id = obj.teacher_id
        course_id = obj.course_id

        course = Courses.objects.get(id=course_id)
        teacher = Teacher.objects.get(id=teacher_id)

        teacher.total_money -= course.teacher_money
        teacher.total_hour -= course.total_time

        obj.save()
        teacher.save()

    # 重写delete_model根据缺勤更新教师的课时和课时费
    def delete_model(self):
        """重写delete_model根据缺勤更新教师的课时和课时费"""
        obj = self.obj

        teacher_id = obj.teacher_id
        course_id = obj.course_id

        course = Courses.objects.get(id=course_id)
        teacher = Teacher.objects.get(id=teacher_id)

        teacher.use_hour += course.total_time
        teacher.remain_hour -= course.total_time
        teacher.remain_money -= course.student_money

        obj.delete()
        teacher.save()

xadmin.site.register(models.TeacherAbsences, TeacherAbsencesAdmin)
