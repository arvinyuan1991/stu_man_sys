import xadmin

# Register your models here.
from absences import models
from courses.models import Courses
from students.models import Student


class AbsencesAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['id', 'student', 'course']
    list_per_page = 5
    ordering = ['id']

    # 重写save_models根据缺勤更新学生的课时和课时费
    def save_models(self):
        """重写save_models根据缺勤更新学生的课时和课时费"""
        obj = self.new_obj
        student_id = obj.student_id
        course_id = obj.course_id

        course = Courses.objects.get(id=course_id)
        student = Student.objects.get(id=student_id)

        student.use_hour -= course.total_time
        student.remain_hour += course.total_time
        student.remain_money += course.student_money

        obj.is_delete = False
        obj.save()
        student.save()

    # 重写delete_model根据缺勤更新学生的课时和课时费
    def delete_model(self):
        """重写delete_model根据缺勤更新学生的课时和课时费"""
        obj = self.obj

        student_id = obj.student_id
        course_id = obj.course_id

        course = Courses.objects.get(id=course_id)
        student = Student.objects.get(id=student_id)

        student.use_hour += course.total_time
        student.remain_hour -= course.total_time
        student.remain_money -= course.student_money

        obj.delete()
        student.save()


xadmin.site.register(models.StudentAbsences, AbsencesAdmin)
