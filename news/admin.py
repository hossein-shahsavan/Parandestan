from django.contrib import admin
from .models import News


# Register your models here.

@admin.register(News)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'show', 'created')
    list_editable = ('show',)
    list_filter = ('show', 'created')
    search_fields = ('news_title',)
    prepopulated_fields = {'slug': ('news_title',)}
