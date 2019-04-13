import xadmin

# Register your models here.
from clastudent import models


class ClassStudentAdmin(object):
    list_display = ['id', 'classes', 'student']
    model_icon = 'fa fa-gift'
    ordering = ['id']
    list_per_page = 5


xadmin.site.register(models.ClassStudent, ClassStudentAdmin)
