#!/usr/bin/python3
#-*-coding:utf-8-*-
#@File: urls.py
#@Author:duzhongqiu
#@time: 2019-01-27 11:43

from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('index/',views.index),
]
