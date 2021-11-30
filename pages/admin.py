from django.contrib import admin
#from django.contrib.admin import register
from .models import Page

#@register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)