from django.db import models
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

#个人信息
class Basicinfo(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    marry = (
        ('yes', "是"),
        ('no', "否"),
    )
    localstate = (
        ('service',"在职，看看新机会"),
        ('leave',"正在离职，一个月内到岗"),
        ('leaved',"已离职，随时到岗"),
    )
    name = models.CharField('姓名',max_length=16)#姓名
    birthday = models.DateField('出生日期')#出生日期
    sex = models.CharField('性别',max_length=32, choices=gender, default="男")#性别
    moblie = models.CharField('手机号',max_length=11)#手机号
    email = models.EmailField('邮箱')#邮箱
    location = models.CharField('所在地点',max_length=32)#所在地
    house = models.CharField('户籍',max_length=32)#户籍
    marriage = models.CharField('是否结婚',max_length=32, choices=marry, default="否")#是否已婚
    worktime = models.DateField('开始工作时间')#开始工作日期
    job = models.CharField('求职岗位',max_length=32)#求职岗位
    state = models.CharField('当前状态',max_length=32, choices=localstate, default="在职，看看新机会")#当前状态

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '基本资料'
        verbose_name_plural = '基本资料'

class Education(models.Model):
    degrees = (
        ('primary',"小学"),
        ('junior',"初中"),
        ('high',"高中"),
        ('college',"大专"),
        ('specialist',"专科"),
        ('bachelor',"本科"),
        ('postgraduate',"研究生"),
        ('doctor',"博士"),
    )
    unifieds = (
        ('yes', "是"),
        ('no', "否"),
    )
    institution = models.CharField('院校',max_length=32)#院校
    department = models.CharField('院系',max_length=32)#院系
    profession = models.CharField('专业',max_length=32)#专业
    degree = models.CharField('学历',max_length=32,choices=degrees)
    unified = models.CharField('是否统招',max_length=32,choices=unifieds)
    stating = models.DateField('就读时间')
    ending = models.DateField('毕业时间')
    petname = models.ForeignKey(Basicinfo,verbose_name='姓名',on_delete=models.CASCADE)

    def __str__(self):
        return self.institution
    class Meta:
        verbose_name = '教育背景'
        verbose_name_plural = '教育背景'

class Worklist(models.Model):
    scales = (
        ('fifty',"50人以下"),
        ('hundred',"50-200人"),
        ('thousand',"200-1000人"),
        ('more',"1000人以上"),
    )
    company = models.CharField('公司名称',max_length=32)#公司
    position = models.CharField('职位',max_length=32)#职位
    scale = models.CharField('规模',max_length=32,choices=scales)
    industry = models.CharField('行业',max_length=32)
    salary = models.CharField('薪酬',max_length=32)
    location = models.CharField('工作地点', max_length=32)
    duties = RichTextUploadingField('职责业绩',null=True, blank=True)
    entertime = models.DateField('入职日期')
    leavetime = models.DateField('离职日期',null=True, blank=True)
    petname = models.ForeignKey(Basicinfo, verbose_name='姓名',on_delete=models.CASCADE)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = '工作经历'
        verbose_name_plural = '工作经历'

class Thing(models.Model):

    thingname = models.CharField('项目名称',max_length=32)
    thingposition = models.CharField('项目职务',max_length=32)
    thingdescription = RichTextUploadingField('项目描述', null=True, blank=True)
    thingresponsibility = RichTextUploadingField('项目职责', null=True, blank=True)
    thingperformance = RichTextUploadingField('项目业绩', null=True, blank=True)
    entertime = models.DateField('开始日期')
    leavetime = models.DateField('结束日期',null=True, blank=True)
    workname = models.ForeignKey(Worklist,verbose_name='公司',on_delete=models.CASCADE)

    def __str__(self):
        return self.thingname

    class Meta:
        verbose_name = '项目经历'
        verbose_name_plural = '项目经历'

class Skill(models.Model):
    petname = models.OneToOneField(Basicinfo, verbose_name='姓名',on_delete=models.CASCADE)
    skills = RichTextUploadingField('技能特长', null=True, blank=True)

    def __str__(self):
        return self.skills

    class Meta:
        verbose_name = '技能特长'
        verbose_name_plural = '技能特长'

class Evaluation(models.Model):
    petname = models.OneToOneField(Basicinfo, verbose_name='姓名',on_delete=models.CASCADE)
    evaluations = RichTextUploadingField('自我评价', null=True, blank=True)

    def __str__(self):
        return self.evaluations

    class Meta:
        verbose_name = '自我评价'
        verbose_name_plural = '自我评价'