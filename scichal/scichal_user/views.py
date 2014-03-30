# Robogals Science Challenge
# Custom users
#
# 2014 Robogals Software Team

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.utils import timezone

from scichal_cms.models import Component

def register(request):
    menu_items = Component.objects.filter(enabled=True, menu_order__gt=0)
    
    time_now = timezone.now
    time_now_year = time_now.year
    
    dob_year_select_range = range((time_now_year-120),time_now_year+1)
    dob_year_select_default = time_now_year-12
    
    template = 'register.html'
    
    try:
        return render(request, template, {
            'title': 'Register',
            'show_title': true,
            'menu_items': menu_items,
            'dob_year_select_range': dob_year_select_range,
            'dob_year_select_default': dob_year_select_default,
            })
    except TemplateDoesNotExist:
        raise Http404('Template "{}" does not exist.'.format(requested_page.template))
