from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.models import Group

from django.views.generic import RedirectView

admin.autodiscover()

# Hide groups (unused)
admin.site.unregister(Group)

# Set patterns for URLs
urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    
    # Account management, Registration
    url(r'^register/$', 'scichal_user.views.register', name='register'),
    
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='account_page_display')),
    url(r'^accounts/$', 'scichal_user.views.account_page_display', name='account_page_display'),
    
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    
    url(r'^accounts/reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'password_reset.html'}, name='password_reset'),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^accounts/reset/sent/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'password_reset_sent.html'}, name='password_reset_done'),
    url(r'^accounts/reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'password_reset_done.html'}, name='password_reset_complete'),
    
    url(r'^accounts/password/$', 'django.contrib.auth.views.password_change', {'template_name': 'password_change.html'}, name='password_change'),
    url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'password_change_done.html'}, name='password_change_done'),

    # Challenges (submissions)
    url(r'^challenges/$', 'scichal_cms.views.page_render', kwargs=dict(resource_id='challenges')),
    #url(r'^challenges/list/$', 'scichal_submission.views.submissiontype_list'),
    #url(r'^challenges/(?P<resource_id>.+?)/submit/$', 'scichal_submission.views.submission_submit'),
    url(r'^challenges/(?P<resource_id>.+?)/(?P<id>\d+)/$', 'scichal_submission.views.submission_display'),
    url(r'^challenges/(?P<resource_id>.+?)/$', 'scichal_submission.views.submissiontype_display_info'),
    
    
    
    # Custom basic CMS
    # Catches all other URLs, and assumes / to point to /home
    url(r'^$', 'scichal_cms.views.page_render', kwargs=dict(resource_id='home')),
    url(r'^(?P<resource_id>.+?)/$', 'scichal_cms.views.page_render'),
)