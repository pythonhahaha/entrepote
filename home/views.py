# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def show_view(request):
    return render(request,'login.html')
def home_viewx(request):
    uname = request.POST.get('userNum', '')
    pwd = request.POST.get('userPw', '')
    response = HttpResponse()
    if uname == 'admin' and pwd == 'admin123':
        return render(request, 'base.html')
    return redirect('/')

def a_view(request):
    return render(request,'top.html')


def b_view(request):
    return render(request, 'left.html')


def c_view(request):
    return render(request, 'down.html')


def centera_view(request):
    return render(request,'index1.html')


def d_view(request):
    return render(request,'center.html')

# 客户信息
def e_view(request):
    customername = CustomerCare.objects.first().customer
    customerinfo = CustomerInfo.objects.all()
    return render(request,'customer.html',{'customerinfo':customerinfo,'customername':customername})

# 客户分配
def f_view(request):
    return render(request,'allocation.html')

# 客户关怀
def g_view(request):
    customercare = CustomerCare.objects.all()
    return render(request,'care.html',{'customercare':customercare})

# 客户类型
def h_view(request):
    customertype = CustomerType.objects.all()
    return render(request,'type.html',{'customertype':customertype})

# 客户状态
def i_view(request):
    customercondition = CustomerCondition.objects.all()
    return render(request,'state.html',{'customercondition':customercondition})

# 客户来源
def j_view(request):
    customersource = CustomerSource.objects.all()
    return render(request,'source.html',{'customersource':customersource})


def k_view(request):
    return render(request,'message.html')

# 房屋信息
def l_view(request):
    housetype = HouseInfo.objects.first().type
    houseuser = HouseInfo.objects.first().user
    houseinfo = HouseInfo.objects.all()
    return render(request,'house.html',{'houseinfo':houseinfo},{'housetype':housetype},{'houseuser':houseuser})

# 房屋类型
def m_view(request):
    housetype = HouseType.objects.all()
    return render(request,'hometype.html',{'housetype':housetype})

# 部门信息
def n_view(request):
    department = DepartmentInfo.objects.all()
    return render(request,'section.html',{'department':department})

# 公告
def o_view(request):
    notice = NoticeInfo.objects.all()
    return render(request,'notice.html',{'notice':notice})


def p_view(request):
    return render(request,'employees.html')


def q_view(request):
    return render(request,'branch.html')


def r_view(request):
    return render(request,'role.html')