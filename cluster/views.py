from django.shortcuts import render
from .models import ImageList
from django.http import JsonResponse


# Create your views here.

def show_image(request):
    res = {'data': ''}
    Img = ImageList.objects.all()
    for img in Img:
         pass
    print(Img)
    res['data'] = Img
    return JsonResponse(res)
