from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
#@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    #empty_value_display = '-empty-'
    #fields = ('title', )
    #exclude = ('title', )
    list_display = ('title', 'author', 'counted_view', 'status', 'login_require',  'published_date', 'created_date')
    list_filter = ('status', 'author')
    #ordering = ['created_date']
    #ordering = ['-created_date']
    search_fields = ['title', 'content']
    summernote_fields = ['content']

class CommectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date')
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post']

admin.site.register(Comment, CommectAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)

