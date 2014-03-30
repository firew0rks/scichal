# Robogals Science Challenge
# Custom users
#
# 2014 Robogals Software Team

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from django.utils import timezone

from scichal_cms.models import Component

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/profile/')
    
    menu_items = Component.objects.filter(enabled=True, menu_order__gt=0)
    
    time_now = timezone.now()
    time_now_year = time_now.year
    
    dob_year_select_range = range((time_now_year-100),time_now_year+1)
    dob_year_select_selected = time_now_year-10
    
    template = 'register.html'
    
    try:
        return render(request, template, {
            'title': 'Register',
            'show_title': True,
            'menu_items': menu_items,
            'dob_year_select_range': dob_year_select_range,
            'dob_year_select_selected': dob_year_select_selected,
            })
    except TemplateDoesNotExist:
        raise Http404('Template "{}" does not exist.'.format(requested_page.template))

def account_page_display(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')

    menu_items = Component.objects.filter(enabled=True, menu_order__gt=0)
    
    template = 'profile.html'
    
    try:
        return render(request, template, {
            'title': 'Profile',
            'show_title': True,
            'menu_items': menu_items,
            'user': request.user,
            })
    except TemplateDoesNotExist:
        raise Http404('Template "{}" does not exist.'.format(requested_page.template))