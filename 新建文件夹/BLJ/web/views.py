from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.decorators import login_required
# 用来验证登陆
from web import models
from backend.multitask import MultiTaskManger
import json

def dashboard(request):
    '''主页'''
    return render(request,'index.html')


def web_ssh(request):
    return render(request, 'web_ssh.html')
def acc_login(request):
    error_msg = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            error_msg = "用户名错误,或密码错误"


    return render(request,'login.html',{'error_msg':error_msg})


@login_required
def host_mgr(request):
    return render(request,'host_mgr.html')


@login_required

def file_transfer(request):
    return render(request, 'file_transfer.html')

@login_required
def batch_task_mgr(reqeust):
    '''获取命令返回结果'''

    task_data=json.loads(reqeust.POST.get('task_data'))
    task_obj=MultiTaskManger(reqeust)
    response = {
        'task_id': task_obj.task_obj.id,
        'selected_hosts': list(task_obj.task_obj.tasklogdetail_set.all().values('id',

                                                                                'host_to_remote_user__host__ip_addr',
                                                                                'host_to_remote_user__host__hostname',
                                                                                'host_to_remote_user__remote_user__username')
                               )
    }


    return HttpResponse(json.dumps(response))

def task_result(request):
    task_id = request.GET.get('task_id')


    sub_tasklog_objs = models.TaskLogDetail.objects.filter(task_id=task_id)

    #log_data = sub_tasklog_objs.values('id','status','result','date')
    log_data = list(sub_tasklog_objs.values('id','status','result'))

    return HttpResponse(json.dumps(log_data))
