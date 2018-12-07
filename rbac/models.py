from django.db import models


# Create your models here.


class AbUserInfo(models.Model):
    """
    用户表
    roles 字段： 用户和角色多对多字段，这个字段可以写在用户表或者角色表中，主要看场景是根据角色找用户还是根据用户找角色，
                在这个场景中，我们根据用户找角色多，所以我们把ManyToManyField字段写在用户表中
        null = True ： 允许为空
        blank = True： 在django Admin后台允许为空
    """
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=64, verbose_name="密码")
    roles = models.ManyToManyField(to="Role", null=True, blank=True, verbose_name="用户角色")

    def __str__(self):
        """
        在Django Admin中显示数据名称
        :return:
        """
        return self.username

    class Meta:
        """
        在Django Admin中显示中文表名
        """
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


class Role(models.Model):
    """
    角色权限表
    Permissions: 角色和权限URL是多对多的关系，在这个场景中我们使用角色查找URL，所以我们把ManyToManyField写在角色表中
    """
    name = models.CharField(max_length=36, verbose_name="角色名称")
    Permissions = models.ManyToManyField(to="Permission", verbose_name="权限URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "角色表"
        verbose_name_plural = verbose_name


class Permission(models.Model):
    """
    权限表
    保存需要控制的URL
    """
    name = models.CharField(max_length=16, verbose_name="UR名称")
    url = models.CharField(max_length=255, verbose_name="URL路径")
    is_menus = models.BooleanField(default=False, verbose_name="是否可作为菜单？")
    icon = models.CharField(max_length=255, verbose_name="菜单图标", null=True, blank=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "权限表"
        verbose_name_plural = verbose_name
