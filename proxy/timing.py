#!/usr/bin/python3
#-*-coding:utf-8-*-
#@File: timing.py
#@Author:duzhongqiu
#@time: 2019-01-29 15:35
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendemail():
    message = MIMEText('Django 后台邮件', 'plain', 'utf-8')
    message['From'] = Header("email sender", 'utf-8')
    message['To'] = Header("email receiver", 'utf-8')

    subject = 'Django 后台自动邮件发送测试...'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(settings.MAIL_HOST, 25)  # 25 为 SMTP 端口号
        smtpObj.login(settings.MAIL_USER,settings.MAIL_PASS)
        smtpObj.sendmail(settings.SENDER,settings.RECEIVERS, message.as_string())
    except smtplib.SMTPException:
        pass
