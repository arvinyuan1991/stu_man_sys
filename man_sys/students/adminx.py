import xadmin

from xadmin import views

# Register your models here.

from students import models


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "师生管理系统"  # 设置站点标题
    site_footer = "郢苏科技"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)


# 注册student类
class StudentAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['id', 'name', 'age', 'gender', 'total_money', 'remain_money', 'total_hour', 'use_hour',
                    'remain_hour']
    search_fields = ['name']


xadmin.site.register(models.Student, StudentAdmin)
