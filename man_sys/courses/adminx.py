import xadmin

# Register your models here.
from courses import models


class CoursesAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['id', 'title', 'subject', 'classes', 'teacher', 'start_time', 'end_time', 'class_room', 'subject',
                    'total_time', 'student_money', 'teacher_money']
    search_fields = ['title']
    list_per_page = 5
    ordering = ['start_time']


xadmin.site.register(models.Courses, CoursesAdmin)
