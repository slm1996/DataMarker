from django.conf import settings


def init_permission(request, user_obj):
    """
    初始化rbac
        1. 根据用户对象，取到用户对应的角色，根据角色在取到对应的权限。最后distinct做一个去重处理
        2. permission_list 定义一个用来存储用户权限的列表
        3. menus_list 定义一个用来存储用户菜单的列表
        4. 循环ret，添加权限和菜单到对应的列表
        5. 保存权限列表和菜单列表到session中
        备注：使用settings来存session的key方便在其他模块中调用
    :param request: 用户请求对象
    :param user_obj: 用户orm对象
    :return:
    """
    ret = user_obj.roles.all().values(
        "Permissions__name",
        "Permissions__url",
        "Permissions__is_menus",
        "Permissions__icon"
    ).distinct()

    permission_list = []
    menus_list = []

    for item in ret:
        permission_list.append({"Permissions__url": item["Permissions__url"]})  # 添加到权限列表
        if item["Permissions__is_menus"]:  # 如果当前循环的权限可以作为菜单展示
            menus_list.append({  # 把当前权限的信息添加到菜单列表
                "name": item["Permissions__name"],
                "icon": item["Permissions__icon"],
                "url": item["Permissions__url"]
            })
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menus_list