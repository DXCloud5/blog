from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','pub_time','author','art_class']
    list_filter = ('pub_time','art_class')




admin.site.register(Article,ArticleAdmin)