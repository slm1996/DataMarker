from django.db import models


# Create your models here.

class ImageList(models.Model):
    img = models.FileField(upload_to='images1', verbose_name='图片上传路径')

    class Meta:
        verbose_name = '图片列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.img


class EditImgList(models.Model):
    img_list = models.ForeignKey(ImageList)
    img = models.FileField(upload_to='images2', verbose_name='编辑区图片存放')

    class Meta:
        verbose_name = '编辑区图片列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.img
