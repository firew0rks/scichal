# Robogals Science Challenge
# Custom basic CMS
#
# 2014 Robogals Software Team

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist

from .models import Component

def page_render(request, resource_id):
    requested_page = get_object_or_404(Component, resource_id=resource_id, enabled=True)
    menu_items = Component.objects.filter(enabled=True, menu_order__gt=0)
    
    template = requested_page.template if requested_page.template else 'standard.html'
    
    try:
        return render(request, template, {
            'title': requested_page.title,
            'show_title': requested_page.title_display_head,
            'body_class': requested_page.body_class,
            'body': requested_page.body,
            'menu_items': menu_items,
            })
    except TemplateDoesNotExist:
        raise Http404('Template "{}" does not exist.'.format(requested_page.template))
