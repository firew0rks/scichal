# Robogals Science Challenge
# Submissions for challenges and submission groups
#
# 2014 Robogals Software Team

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from django.contrib.formtools.wizard.views import SessionWizardView

from datetime import date, timedelta

from .models import SubmissionType, Submission, AgeCategory

import scichal_submission.forms

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
                         ]
                            # ("SubmissionEntry3", scichal_submission.forms.SubmissionEntry3),
                            # ("SubmissionEntry4", scichal_submission.forms.SubmissionEntry4),
                            # ("SubmissionEntry5", scichal_submission.forms.SubmissionEntry5),
                            # ("SubmissionEntryConfirm", scichal_submission.forms.SubmissionEntryConfirm)
                         # ]

SUBMISSION_ENTRY_TEMPLATES = {  "SubmissionEntry1": "submission_entry_standard.html",
                                "SubmissionEntry2": "submission_entry_standard.html",
                             }
                                # "SubmissionEntry3": "submission_entry_standard.html",
                                # "SubmissionEntry4": "submission_entry_standard.html",
                                # "SubmissionEntry5": "submission_entry_standard.html",
                                # "SubmissionEntryConfirm": "submission_entry_confirmation.html"
                             # }

class SubmissionEntryWizard(SessionWizardView):
    def get_template_names(self):
        return [SUBMISSION_ENTRY_TEMPLATES[self.steps.current]]
    
    def get_form_initial(self, step):
        initial_vals = { }

        if step == "SubmissionEntry2":
            # Prefill with appropriate age category
            user_dob = self.request.user.dob
            
            if user_dob:
                user_age_years = int((date.today() - user_dob).days / 365.2425)    # http://stackoverflow.com/a/4828842
                
                try:
                    age_category_obj = AgeCategory.objects.get( age_min__lte=user_age_years, age_max__gte=user_age_years )
                    initial_vals = { "age_category": age_category_obj }
                except AgeCategory.DoesNotExist:
                    # Skip for invalid/unaccounted ages
                    pass
                    
        return initial_vals
    
    # def get_form(self, step=None, data=None, files=None):
        # form = super(SubmissionEntryWizard, self).get_form(step, data, files)
        
        # if step == "SubmissionEntry2":
            # form.fields['checkbox_2'].widget.attrs['disabled'] = 'disabled'
        
        # return form
        
    
    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('/home/')      ## Change when complete
        
        