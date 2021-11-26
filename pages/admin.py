from django.contrib import admin
#from django.contrib.admin import register
from .models import Page

#@register(Page)
class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)