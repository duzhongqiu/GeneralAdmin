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
    list_display = ('title','category','content','pub')
    search_fields = ('title',)
    list_filter = ('title','category','content','pub')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','name','content','pub')
    search_fields = ('name',)
    list_filter = ('blog','name','content','pub')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)