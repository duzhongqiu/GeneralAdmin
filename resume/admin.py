from django.contrib import admin
from .models import *
# Register your models here.

class BasicinfoAdmin(admin.ModelAdmin):
    list_display = ('name','birthday','sex','moblie','email','location','house','marriage','worktime','job','state')
    search_fields = ('name',)
    list_filter = ('name','birthday','sex','moblie')
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution','department','profession','degree','unified','stating','ending','petname')
    search_fields = ('institution',)
    list_filter = ('institution','department','profession')
class WorklistAdmin(admin.ModelAdmin):
    list_display = ('company','position','scale','industry','salary','location','entertime','leavetime','petname')
    search_fields = ('company',)
    list_filter = ('company','position','scale')
class ThingAdmin(admin.ModelAdmin):
    list_display = ('thingname','thingposition','thingperformance','entertime','leavetime','workname')
    search_fields = ('thingname',)
    list_filter = ('thingname','thingposition','thingperformance')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('petname','skills')
    search_fields = ('petname',)
    list_filter = ('petname',)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('petname','evaluations')
    search_fields = ('petname',)
    list_filter = ('petname',)


admin.site.register(Basicinfo,BasicinfoAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Worklist,WorklistAdmin)
admin.site.register(Thing,ThingAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Evaluation,EvaluationAdmin)