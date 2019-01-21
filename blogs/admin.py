from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','标签','pub')
    search_fields = ('title',)
    list_filter = ('category','tag','pub')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','name','content','pub')
    search_fields = ('blog',)
    list_filter = ('name','pub')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)