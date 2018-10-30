import os
import pymysql

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DataMarker.settings")
# import django
import random

# django.setup()
# from user import models

image_list = os.listdir(r"C:\Users\Mr.Ming\Desktop\DataMarker\media/images/")
ran = random.sample(image_list, 1)
# print(random.sample(image_list, 1))
print(ran)

f = open(r"C:\Users\Mr.Ming\Desktop\DataMarker\media/images/20180719_IMG_1426.JPG", 'rb')
img = f.read()
f.close()
try:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        # db='data_marker',
        db='test',
        charset='utf8',
        use_unicode=True
    )
    cursor = conn.cursor()
    # with open(r'C:\Users\Mr.Ming\Desktop\DataMarker\media/images/20180719_IMG_1815.JPG', 'rb') as f:
    #     data = f.read()
    cursor.execute('INSERT INTO picture(image) values("%s")' % img)
    conn.commit()
    cursor.close()
    conn.close()
except Exception as e:
    # print("Error %d: %s" % (e.args[0], e.args[1]))
    print(e)