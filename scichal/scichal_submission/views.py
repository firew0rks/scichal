# Robogals Science Challenge
# Submissions for challenges and submission groups
#
# 2014 Robogals Software Team

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist

from .models import SubmissionType,Submission
from scichal_cms.models import Component

def submissiontype_display_info(request, resource_id):
    requested_submissiontype = get_object_or_404(SubmissionType, resource_id=resource_id, info_page_visible=True)
    submissions = Submission.objects.filter(submission_type=requested_submissiontype)
    
    template = 'challenge_display.html'
    
    try:
        return render(request, template, {
            'title': requested_submissiontype.name,
            'body': requested_submissiontype.info_page.body,
            'submissions': submissions,
            'menu_items': Component.objects.filter(enabled=True, menu_order__gt=0),
            })
    except TemplateDoesNotExist:
        raise Http404('Template "{}" does not exist.'.format(requested_page.template))

def submission_display(request, resource_id, id):
    requested_submission = get_object_or_404(Submission, id=id)
    
    template = 'challenge_submission_display.html'
    
    try:
        return render(request, template, {
            'submission': requested_submission,
            'menu_items': Component.objects.filter(enabled=True, menu_order__gt=0),
            })
    except TemplateDoesNotExist:
        raise Http404('Template "{}" does not exist.'.format(requested_page.template))
