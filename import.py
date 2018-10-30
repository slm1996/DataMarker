import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DataMarker.settings")
    import django
    django.setup()
    from user import models

    image_list = os.listdir(r"C:\Users\Mr.Ming\Desktop\DataMarker\media/images/")
    for i in image_list:
        models.Image.objects.create(image_url="images/{}".format(i))
