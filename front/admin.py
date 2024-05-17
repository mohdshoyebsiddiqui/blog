from django.contrib import admin
from .models import Article,Cate

# Register your models here.

class ArticleField(admin.ModelAdmin):
    list_display=['title', 'des', 'date' ]

admin.site.register(Article,ArticleField)
admin.site.register(Cate)

