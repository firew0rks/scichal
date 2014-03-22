# Robogals Science Challenge
# Custom basic CMS
#
# 2014 Robogals Software Team

from django.contrib import admin

from .models import Component

class ComponentAdmin(admin.ModelAdmin):
    list_display = ('resource_id', 'title', 'menu_order', 'enabled')
    search_fields = ('resource_id', 'title')
    ordering = ('-enabled', 'resource_id', 'menu_order')
    
    fieldsets = [
        ('Basic information',   {'fields': ['resource_id', 'title', 'body', 'enabled']}),
        ('Additional options',  {'fields': ['title_display_head', 'menu_order', 'body_class', 'template'], 'classes': ['collapse']}),
    ]
    
admin.site.register(Component, ComponentAdmin)