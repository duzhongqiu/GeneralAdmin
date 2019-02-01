#!/usr/bin/python3
#-*-coding:utf-8-*-
#@File: timing.py
#@Author:duzhongqiu
#@time: 2019-01-29 15:35
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
from bs4 import BeautifulSoup
from .import models

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


def getproxy():

    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    for page in range(1,11):
        url = 'https://www.kuaidaili.com/free/inha/'+str(page)+'/'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        iplist = soup.find_all('td', attrs={"data-title": "IP"})
        portlist = soup.find_all('td', attrs={"data-title": "PORT"})
        hidelist = soup.find_all('td', attrs={"data-title": "匿名度"})
        typelist = soup.find_all('td', attrs={"data-title": "类型"})
        addresslist = soup.find_all('td', attrs={"data-title": "位置"})
        speedlist = soup.find_all('td', attrs={"data-title": "响应速度"})
        checklist = soup.find_all('td', attrs={"data-title": "最后验证时间"})
        for num in range(0, len(iplist)):
            selectproxy = models.AgentList.objects.filter(proxyip=iplist[num].text)
            if selectproxy:
                pass
            else:
                obj = models.AgentList(proxyip=iplist[num].text,proxyport=portlist[num].text,proxyaddress=addresslist[num].text,
                                       proxyhide=hidelist[num].text,proxytype=typelist[num].text,proxyspeed=speedlist[num].text,
                                       proxylink='null',proxylive='null',proxycheck=checklist[num].text)
                obj.save()

