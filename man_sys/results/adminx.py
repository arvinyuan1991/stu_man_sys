import xadmin

# Register your models here.
from results import models


class ResultsAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['id', 'name', 'time', 'point', 'subject', 'student', 'comment']
    ordering = ['time']
    list_per_page = 5
    data_charts = {
        'student': {
            "title": '考试成绩', 'x-field': 'time', 'y-field': ('point',), "order": ('time',)
        }
    }


xadmin.site.register(models.Results, ResultsAdmin)
