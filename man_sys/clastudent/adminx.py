import xadmin

# Register your models here.
from clastudent import models


class ClassStudentAdmin(object):
    list_display = ['id', 'classes', 'student']
    model_icon = 'fa fa-gift'
    search_fields = ['classes']
    ordering = ['id']


xadmin.site.register(models.ClassStudent, ClassStudentAdmin)
