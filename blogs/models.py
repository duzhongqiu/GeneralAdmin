from django.db import models
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    #博客的分类
    name = models.CharField('名称',max_length=30)
    def  __str__(self):
        return self.name
    class Meta:
        verbose_name='栏目'
        verbose_name_plural = '栏目'

class Tag(models.Model):
    #博客的标签
    name = models.CharField('名称',max_length=30)
    def  __str__(self):
        return self.name
    class Meta:
        verbose_name='标签'
        verbose_name_plural = '标签'

class Blog(models.Model):
    #博客的内容
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者', max_length=16)
    content = RichTextUploadingField('内容',null=True, blank=True)
    pub = models.DateField('发布时间',auto_now_add=True)
    category = models.ForeignKey(Category,verbose_name='栏目',on_delete=models.CASCADE)#多对一（博客-类别）
    tag = models.ManyToManyField(Tag,verbose_name='标签')
    image = models.ImageField(upload_to='blogimg', verbose_name='图片', null=True)

    def 标签(self):
        return [tag.name for tag in self.tag.all()]
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'

class Welcome(models.Model):
    status_choice = (
        ('line', '是'),
        ('notline', '否'),
    )
    title = models.CharField('标题',max_length=32)
    content = models.CharField('内容',max_length=64)
    status = models.CharField('上线',choices=status_choice,max_length=8)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '欢迎语'
        verbose_name_plural = '欢迎语'

class Comment(models.Model):
    #评论
    blog = models.ForeignKey(Blog,verbose_name='博客',on_delete=models.CASCADE)
    name = models.CharField('用户',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=200)
    pub = models.DateField('评论时间',auto_now_add=True)
    def __str__(self):
        return self.content
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'