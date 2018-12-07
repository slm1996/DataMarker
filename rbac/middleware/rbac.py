"""
    自定义RBAC中间件
    功能描述：
        根据用户角色实现权限控制
    """
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse
import re
from django.conf import settings


class RBACMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        自定义中间件
        1. 中间件的描述
            1. 执行时间
                在执行视图函数之前执行
            2. 执行顺序
                按照注册的顺序执行
            3. 参数和返回值
                1. request参数和视图函数中是同一个对象
                2. 返回值：
                    1. 返回None：请求继续往后执行
                    2. 返回响应对象：请求就结束了，要返回响应了
        2. 取到用户的url
            1. 循环白名单
            2. 判断用户当前访问的URL是否在白名单中
            3. 如果在白名单中则返回None代码继续往后执行
        3. 取到用户的访问权限
            1. 如果没有取到登录时存的session，则说明用户没有登录，跳转到登录页面
        :param request:
        :return:
        """
        url = request.path_info

        for i in settings.PERMISSION_WHITE_URL:
            ret = "^{}$".format(i)
            if re.match(ret, url):
                return None

        user_url = request.session.get(settings.PERMISSION_SESSION_KEY)
        if not user_url:
            return redirect("/login/")

        for i in user_url:
            ret = "^{}$".format(i["Permissions__url"])
            if re.match(ret, url):
                return None
            else:
                return HttpResponse("没有权限方法")
