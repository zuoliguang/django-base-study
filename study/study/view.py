# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from datetime import datetime
import json, os

from UserModel.models import User

def hello(request):
    return HttpResponse("Hello world ! ")

def viewHello(request):
    context          = {}
    context['hello'] = 'this is a model view page!'
    context['condition1'] = 0
    context['condition2'] = 0
    context['condition3'] = 0
    context['condition4'] = 0
    context['condition5'] = 0
    context['array'] = [10,0,1,2,3,4,5,6,7,8,9]
    context['a'] = 'aaaaaa'
    context['tempa'] = 'aaaaaa'
    context['b'] = 'bbbbbb'
    context['c'] = 'cccccc'
    context['datetime'] = datetime.now()
    return render(request, 'viewHello.html', context)
    
def dbTest(request):
    # 数据库操作
    response = ""
    response1 = ""

    # 新增
    # user = User(username='test', password='qweasd123456', telphone='12345678901', address='abcdefg', ext='xyz')
    # user.save()
    # return HttpResponse("<p>数据添加成功！</p>")

    # 获取1
    # list = User.objects.all()
    # # 输出所有数据
    # for var in list:
    #     response1 += var.username + " "
    # response = response1
    # return HttpResponse("<p>" + response + "</p>")

    # 获取2
    # User.objects.filter(username="test").order_by("id")
    # list = User.objects.all()
    # # 输出所有数据
    # for var in list:
    #     response1 += var.username + " "
    # response = response1
    # return HttpResponse("<p>" + response + "</p>")

    # 获取3
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = User.objects.filter(id=1) 
    # return HttpResponse(response2)
    # 获取单个对象
    # response3 = User.objects.get(id=1) 
    # return HttpResponse(response3)
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # response4 = User.objects.order_by('username')[0:2]
    # return HttpResponse(response4)

    # 更新
    # user = User.objects.get(id=1)  # 更新1
    # user.username = 'Google'
    # user.save()
    # User.objects.filter(id=2).update(username='Baidu') # 更新2
    # return HttpResponse("<p>修改完成</p>")

    # 删除
    # user = User.objects.get(id=6) # 删除1
    # user.delete()
    User.objects.filter(id=7).delete() # 删除2
    return HttpResponse("<p>删除 完成</p>")

def table_form(request):
    return render_to_response('tableForm.html') # 表单页面

def search_get(request):
	# 处理表单提交信息
    request.encoding='utf-8'
    if 'string' in request.GET:
        message = '你搜索的内容为: ' + request.GET['string']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['key']
    return render(request, "tableForm.html", ctx)

def viewInit(request):
    path = os.getcwd()
    return HttpResponse(path)