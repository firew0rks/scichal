# Robogals Science Challenge
# Submissions for challenges and submission groups
#
# 2014 Robogals Software Team

from django.contrib import admin

from .models import SubmissionType,Submission

class SubmissionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'resource_id', 'max_users', 'date_open', 'date_close',)
    search_fields = ('name', 'resource_id',)
    ordering = ('resource_id',)
    
    raw_id_fields = ('info_page',)
    
    fieldsets = [
        ('Basic information',   {'fields': ['name', 'resource_id', 'info_page', 'info_page_visible', 'submission_view_template', 'date_open', 'date_close']}),
        ('Additional options',  {'fields': ['max_users', 'allows_youtube', 'allows_images'], 'classes': ['collapse']}),
    ]
    
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'submission_type', 'date_submitted',)
    search_fields = ('title', 'body',)
    ordering = ('-date_submitted',)
    
    raw_id_fields = ('submission_type',)
    filter_horizontal = ('users',)
    
    fieldsets = [
        ('Basic information',   {'fields': ['title', 'submission_type', 'users', 'body']}),
        ('Multimedia',          {'description': 'Multimedia should be filled in for entries. Images are only used for fallback.',
                                 'fields': ['youtube_id', 'image']}),
    ]
    
admin.site.register(SubmissionType, SubmissionTypeAdmin)
admin.site.register(Submission, SubmissionAdmin)
