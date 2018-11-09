from django.db import models
from django.contrib.auth.models import AbstractUser,User


class UserInfo(AbstractUser):

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name


class TaskType(models.Model):
    face_attr = models.CharField(max_length=64, verbose_name='人脸属性')
    body_attr = models.CharField(max_length=64, verbose_name='人体属性')

    class Meta:
        verbose_name = '任务类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.face_attr


class Image(models.Model):
    image_url = models.FileField(upload_to='images', verbose_name='图片上传路径')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image


class Coord(models.Model):
    x = models.CharField(max_length=20, null=False, verbose_name='x轴坐标')
    y = models.CharField(max_length=20, null=False, verbose_name='y轴坐标')
    w = models.CharField(max_length=20, null=False, verbose_name='图片宽度')
    h = models.CharField(max_length=20, null=False, verbose_name='图片高度')
    img = models.CharField(max_length=64, verbose_name='所标图片')

    class Meta:
        verbose_name = '坐标管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.x
