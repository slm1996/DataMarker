from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Image, Coord, UserInfo
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.contrib import auth
from .form import UserForm
import time


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)
#         print(user)
#         if user is not None and user.is_active:
#             auth.login(request, user)
#
#             return redirect('/tagPage/', {'user': user})
#         else:
#             error = '用户名或者密码错误!!!'
#             return render(request, 'login.html', {'error': error})
#     elif request.method == 'GET':
#
#         return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = UserInfo.objects.create_user(username=username, password=password)


def login_view(request):
    if request.method == 'POST':
        # uf = UserForm(request.POST)
        # if uf.is_valid():
        #     username = uf.cleaned_data['username']
        #     password = uf.cleaned_data['password']
        #     user_obj = User.objects.filter(username=username, password=password).first()
        #     if user_obj:
        #         auth.login(request, user_obj)
        #         return redirect('/tagPage/')
        # user_obj = auth.authenticate(username=username, password=pwd)
        # if user_obj is not None:
        #     auth.login(request, user_obj)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = UserInfo.objects.filter(username=username, password=password).first()
        # user_obj = auth.authenticate(username=username, password=password)
        if user_obj:
            # auth.login(request, user_obj)
            # auth.authenticate(user_obj)

            return redirect('/tagPage/', {'user': user_obj})
        else:
            error = '用户名或者密码错误!!!'
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def tag_page_turn(request):
    con = {"code": 0}
    if request.method == 'POST':
        print(request.POST.get("id"))  # 第一次当前ID36
        print(request.POST.get('btn'))
        if request.POST.get('btn') == 'next':
            next_id = int(request.POST.get("id")) + 1
            next_obj = Image.objects.filter(id=next_id).first()  # 拿到下一张图片的对象
        else:
            next_id = int(request.POST.get("id")) - 1
            next_obj = Image.objects.filter(id=next_id).first()  # 拿到下一张图片的对象
        if not next_obj:  # 判断对象存不存在
            return JsonResponse(con)

        coord = Coord.objects.all()
        clist = []
        for coo in coord:
            print(coo)
            cx = coo.x
            cy = coo.y
            cw = coo.w
            ch = coo.h
            cimg = coo.img
            print(cx, cy, cw, ch, cimg)
            clist.append(cx)
            clist.append(cy)
            clist.append(cw)
            clist.append(ch)
            clist.append(cimg)
        con["code"] = 1
        con["data"] = {
            "id": next_obj.id,  # 返回下一张或者上一张图片的ID
            "image_url": str(next_obj.image_url),  # 返回下一张或者上一张图片的URL
            "clist": clist
        }
        return JsonResponse(con)

    return render(request, 'tagPage.html')


def tag_page(request):
    if request.method == 'POST':
        print(request.POST.get('res'))
        result = request.POST.get('res')
        img = request.POST.get('img')
        result = json.loads(result)
        # print(result[0])
        print(result[0]['x'])
        print(result[0]['y'])
        print(result[0]['w'])
        print(result[0]['h'])
        coord = Coord()
        coord.x = result[0]['x']
        coord.y = result[0]['y']
        coord.w = result[0]['w']
        coord.h = result[0]['h']
        coord.img = img
        coord.save()

    return render(request, 'tagPage.html')


# def get_frame(request):
#     coord = {}
#     if request.method == 'POST':
#         c = Coord()
#         c1 = c.x
#         c2 = c.y
#         c3 = c.w
#         c4 = c.h
#         image_coord = c.img
#         coord['data'] = {
#             'x': c1,
#             'y': c2,
#             'w': c3,
#             'h': c4,
#             'img': image_coord
#
#         }
#         return JsonResponse(coord)
#
#     return render(request, 'tagPage.html')


def faceShow(request):
    images = Image.objects.all()
    # limit = 5
    p = Paginator(images, 5)
    # p.count
    # p.num_pages
    # p.page_range
    page_num = request.GET.get('page')

    try:
        image_list = p.page(page_num)
    except PageNotAnInteger:
        image_list = p.page(1)
    except EmptyPage:
        image_list = p.page(page_num)

    return render(request, 'faceCluster.html', locals())
