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

    pass
    print 'host 列表'
    appId = {'app_id': 3}

    hosts = client.cc.get_app_host_list(appId)
    print  hosts

    pass
    print 'task 列表'
    tasks = client.job.get_task(appId)
    print  tasks



    print result

    return render_mako_context(request, '/home_application/test_magicbox.html',{"hosts":hosts,"tasks":tasks})


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

def getHosts(request):
    """
    获取host列表
    """
    pass
    print 'host 列表'
    appId = {'app_id': 3}

    client = get_client_by_request(request)

    hosts = client.cc.get_app_host_list(appId)
    print  hosts

    return render_json(hosts)

def getJobs(request):
    """
    获取job列表
    """
    pass
    print 'tasks 列表'
    appId = {'app_id': 3}

    client = get_client_by_request(request)

    tasks = client.job.get_task(appId)
    print  tasks

    return render_json(tasks)

def executeJob(request):
    """
    执行job
    """
    pass
    appId = {'app_id': 3}

    client = get_client_by_request(request)

    #"host":hostIp,"task":taskid
    hostIp = request.POST.get("host")
    taskId = request.POST.get("task")


    task_detail_request = {
        "app_id": 3,
        "task_id": taskId
    }
    tasksDetail = client.job.get_task_detail(task_detail_request)

    print 'tasks 详情'
    #print tasksDetail
    print tasksDetail['data']

    jobTask = {
        "app_id": 3,
        "task_id": taskId,
        "steps": [{
            "scriptTimeout": 1000,
            "scriptParam": "-a",
            "serverSetId": 0,
            "ipList": "1:10.105.34.6,1:10.237.226.14",
            "scriptId": 203,
            "stepId": tasksDetail['data']['nmStepBeanList'][0]['stepId'],
            "account": "root",
        }]
    }

    print 'stepid ..is %d' % tasksDetail['data']['nmStepBeanList'][0]['stepId']

    print len(tasksDetail['data']['nmStepBeanList'])

    execute_task_request = {
        "app_id": 3,
        "task_id": taskId,
        "steps": [{
            "stepId": tasksDetail['data']['nmStepBeanList'][0]['stepId'],
            "ipList":"1:"+hostIp
        }]
    }
    execute_task_response = client.job.execute_task(execute_task_request)

    pass
    print execute_task_response

    taskInstanceId = execute_task_response['data']['taskInstanceId']

    print "task 返回实例id  %d" % taskInstanceId

    get_task_result_request = {
        "task_instance_id": taskInstanceId
    }
    get_task_result_response = client.job.get_task_result(get_task_result_request)

    print "查询task 返回结果是"
    print  get_task_result_response


    get_task_ip_log_request = {
        "task_instance_id":taskInstanceId
    }
    get_task_ip_log_response = client.job.get_task_ip_log(get_task_ip_log_request)

    print "task ip log 返回结果是"
    print  get_task_ip_log_response

    return render_json(tasksDetail)

