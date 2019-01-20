from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    #博客的分类
    name = models.CharField('名称',max_length=30)
    def  __str__(self):
        return self.name
    class Meta:
        verbose_name='类别'
        verbose_name_plural = '类别'

class Tag(models.Model):
    name = models.CharField('名称',max_length=30)
    def  __str__(self):
        return self.name
    class Meta:
        verbose_name='标签'
        verbose_name_plural = '标签'

class Blog(models.Model):
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者', max_length=16)
    content = RichTextUploadingField('内容',null=True, blank=True)
    pub = models.DateField('发布时间',auto_now_add=True)
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)#多对一（博客-类别）
    tag = models.ManyToManyField(Tag,verbose_name='标签')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'

class Comment(models.Model):
    blog = models.ForeignKey(Blog,verbose_name='博客',on_delete=models.CASCADE)
    name = models.CharField('称呼',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=240)
    pub = models.DateField('发布时间',auto_now_add=True)
    def __str__(self):
        return self.content
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'