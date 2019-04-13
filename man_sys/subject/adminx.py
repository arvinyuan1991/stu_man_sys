import xadmin

# Register your models here.
from subject import models


class SubjectAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ['id']
    list_per_page = 5


xadmin.site.register(models.Subject, SubjectAdmin)
