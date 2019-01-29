from django.db import models

# Create your models here.


class AgentList(models.Model):
    proxyip = models.CharField('IP地址', max_length=32)
    proxyport = models.CharField('端口', max_length=32)
    proxyaddress = models.CharField('地址', max_length=32)
    proxyhide = models.CharField('隐匿性', max_length=32)
    proxytype = models.CharField('类型', max_length=32)
    proxyspeed = models.CharField('速度', max_length=32)
    proxylink = models.CharField('连接速度', max_length=32)
    proxylive = models.CharField('存活时间', max_length=32)
    proxycheck = models.CharField('验证时间', max_length=32)

    def __str__(self):
        return self.proxyip

    class Meta:
        verbose_name = '代理IP'
        verbose_name_plural = '代理IP'