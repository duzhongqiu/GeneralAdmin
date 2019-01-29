#!/usr/bin/python3
#-*-coding:utf-8-*-
#@File: timing.py
#@Author:duzhongqiu
#@time: 2019-01-29 15:35

from . import models
import requests
from bs4 import BeautifulSoup

def getproxy():
	url = 'https://www.xicidaili.com/nn/'
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

	response = requests.get(url,headers=headers)
	webtext = BeautifulSoup(response.text,'lxml')
	trsoups = webtext.find_all('tr')
	for num in range(1,len(trsoups)):
		tdtext = BeautifulSoup(str(trsoups[num]),'lxml')
		tdsoups = tdtext.find_all('td')
		proxyip = tdsoups[1].text
		proxyport = tdsoups[2].text
		proxyaddress = tdsoups[3].text.replace('\n','')
		proxyhide = tdsoups[4].text
		proxytype = tdsoups[5].text
		proxylive = tdsoups[8].text
		proxycheck = tdsoups[9].text
		speedsoups = BeautifulSoup(str(tdsoups[6]),'lxml')
		speedsoup = speedsoups.find('div',class_='bar')
		proxyspeed = speedsoup.get('title')
		linksoups = BeautifulSoup(str(tdsoups[7]),'lxml')
		linksoup = linksoups.find('div',class_='bar')
		proxylink = linksoup.get('title')
		selectproxy = models.AgentList.objects.filter(proxyip=proxyip)
		if selectproxy:
			models.AgentList.objects.filter(proxyip=proxyip).update(proxyspeed=proxyspeed,proxylink=proxylink,proxylive=proxylive,proxycheck=proxycheck)
		else:
			obj = models.AgentList(proxyip=proxyip,proxyport=proxyport,proxyaddress=proxyaddress,proxyhide=proxyhide,proxytype=proxytype,proxyspeed=proxyspeed,proxylink=proxylink,proxylive=proxylive,proxycheck=proxycheck)
			obj.save()

