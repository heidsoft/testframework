# -*- coding: utf-8 -*-

from common.mymako import render_mako_context,render_json
from home_application.models import NgUser
from home_application.ng_task import ngTask,ngTask2
from blueking.component.shortcuts import get_client_by_request

def home(request):
    """
    首页
    """
    #ngTask.delay(4,4)
    allUser = NgUser.objects.all()

    # 默认从django settings中获取APP认证信息：应用ID和应用TOKEN
    # 默认从django request中获取用户登录态bk_token
    client = get_client_by_request(request)
    # 组件参数
    kwargs = {'ApplicationID': 3}
    result = client.opsdemo.listHost(kwargs)
    print result

    return render_mako_context(request, '/home_application/test_magicbox.html',{"users":allUser})


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def useradd(request):
    """
    登录请求
    """
    print("post ........")
    name = request.POST.get("name")
    mypass = request.POST.get("paas")
    print(name)
    print(mypass)

    user1 = NgUser.objects.create(name=name,age=20,password=mypass)

    print user1

    user2 = NgUser(name='heidsoft')
    user2.save()

    print user2
    user2.age=28
    user2.save()
    print user2


    return render_json({"success":1})

def userlist(request):
    """
    登录请求
    """
    print("get ........")
    name = request.POST.get("name")
    mypass = request.POST.get("paas")
    print(name)
    print(mypass)

    user1 = NgUser.objects.create(name=name,age=20,password=mypass)

    print user1

    user2 = NgUser(name='heidsoft')
    user2.save()

    print user2
    user2.age=28
    user2.save()
    print user2


    return render_json({"success":1})

def executeTask(request):
    """
    执行task
    """
    pass
    print '周期性执行....'
    ngTask2(1,2)
    return render_json({"success":True})