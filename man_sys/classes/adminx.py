import xadmin

# Register your models here.
from classes import models


class ClassAdmin(object):
    list_display = ['id', 'name']
    model_icon = 'fa fa-gift'
    search_fields = ['name']
    ordering = ['id']
    list_per_page = 5


xadmin.site.register(models.Class, ClassAdmin)
