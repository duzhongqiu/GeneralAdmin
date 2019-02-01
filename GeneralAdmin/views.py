#!/usr/bin/python3
#-*-coding:utf-8-*-
#@File: views.py
#@Author:duzhongqiu
#@time: 2019-02-01 12:58

from django.shortcuts import render

def error(request):
    return render(request,'error/404.html')