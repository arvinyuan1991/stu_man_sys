import xadmin

# Register your models here.

from teachers import models


class TeacherAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['id', 'name', 'age', 'gender', 'total_money', 'total_hour']
    search_fields = ['name']
    list_per_page = 5
    ordering = ['id']


xadmin.site.register(models.Teacher, TeacherAdmin)
