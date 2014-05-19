# Robogals Science Challenge
# Submissions for challenges and submission groups
#
# 2014 Robogals Software Team

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.contrib.formtools.wizard.views import SessionWizardView

import datetime

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
        

SUBMISSION_ENTRY_FORMS = [  ("SubmissionEntry1", scichal_submission.forms.SubmissionEntry1),
                            ("SubmissionEntry2", scichal_submission.forms.SubmissionEntry2),
                            ]"""   ("SubmissionEntry3", scichal_submission.forms.SubmissionEntry3),
                            ("SubmissionEntry4", scichal_submission.forms.SubmissionEntry4),
                            ("SubmissionEntry5", scichal_submission.forms.SubmissionEntry5),
                            ("SubmissionEntryConfirm", scichal_submission.forms.SubmissionEntryConfirm)
                         ]"""

SUBMISSION_ENTRY_TEMPLATES = {  "SubmissionEntry1": "submission_entry_standard.html",
                                "SubmissionEntry2": "submission_entry_standard.html",
                             }"""   "SubmissionEntry3": "submission_entry_standard.html",
                                "SubmissionEntry4": "submission_entry_standard.html",
                                "SubmissionEntry5": "submission_entry_standard.html",
                                "SubmissionEntryConfirm": "submission_entry_confirmation.html"
                             }"""

@login_required
class SubmissionEntryWizard(SessionWizardView):
    def get_template_names(self):
        return [SUBMISSION_ENTRY_TEMPLATES[self.steps.current]]
    
    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('/home/')      ## Change when complete
        
        