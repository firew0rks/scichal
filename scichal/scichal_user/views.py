# Robogals Science Challenge
# Custom users
#
# 2014 Robogals Software Team

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from scichal_cms.models import Component

import datetime

from .forms import SciChalUserAccountForm, SciChalUserAccountRegisterForm

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/')

    menu_items = Component.objects.filter(enabled=True, menu_order__gt=0)
    
    template = 'register.html'
    
    try:
        if (request.method == 'POST'):
            form = SciChalUserAccountRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'])
                login(request, new_user)
                return HttpResponseRedirect('/accounts/')
        else:
            form = SciChalUserAccountRegisterForm()

        return render(request, template, {
            'title': 'Register',
            'show_title': True,
            'menu_items': menu_items,
            'form': form
        })
    except TemplateDoesNotExist:
        raise Http404('Template "{}" does not exist.'.format(requested_page.template))

@login_required
def account_page_display(request):
    menu_items = Component.objects.filter(enabled=True, menu_order__gt=0)
    
    template = 'account.html'
    
    try:
        return render(request, template, {
            'title': 'Account',
            'show_title': True,
            'menu_items': menu_items,
            'user': request.user,
            })
    except TemplateDoesNotExist:
        raise Http404('Template "{}" does not exist.'.format(requested_page.template))

@login_required
def account_edit_display(request):
    menu_items = Component.objects.filter(enabled=True, menu_order__gt=0)
    
    template = 'account_edit.html'
    
    try:
        if (request.method == 'POST'):
            form = SciChalUserAccountForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/')
        else:
            form = SciChalUserAccountForm(instance=request.user)

        return render(request, template, {
            'title': 'Edit account',
            'show_title': True,
            'menu_items': menu_items,
            'form': form,
        })
    except TemplateDoesNotExist:
        raise Http404('Template "{}" does not exist.'.format(requested_page.template))