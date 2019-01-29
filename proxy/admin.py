from django.contrib import admin
from .models import *
# Register your models here.

class AgentListAdmin(admin.ModelAdmin):
    list_display = ('proxyip','proxyport','proxyaddress','proxyhide','proxytype','proxyspeed','proxylink','proxylive','proxycheck','pub')
    search_fields = ('proxyaddress',)
    list_filter = ('proxyaddress','proxyhide')


admin.site.register(AgentList,AgentListAdmin)