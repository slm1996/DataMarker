from django.contrib import admin
from rbac import models

# Register your models here.
admin.site.register(models.AbUserInfo)
admin.site.register(models.Role)


class PermissionAdmin(admin.ModelAdmin):
    # 告诉Django admin在页面上展示我这张表的哪些字段
    list_display = ["name", "url", "is_menus", "icon"]
    # 在列表页面支持直接修改的字段
    list_editable = ["url", "is_menus", "icon"]