import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DataMarker.settings")
    import django
    django.setup()
    from cluster import models

    image_list = os.listdir(r"D:\images")
    print(image_list)
    for i in image_list:
        models.ImageList.objects.create(img="images1/{}".format(i))
