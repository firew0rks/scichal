# Robogals Science Challenge
# Submissions for challenges and submission groups
#
# 2014 Robogals Software Team

from django import forms

from datetime import date

from .models import SubmissionType, AgeCategory, SUBMISSION_GROUP_TYPE

class SubmissionEntry1(forms.Form):
    """Choose a challenge to begin with."""
    available_challenges = forms.ModelChoiceField(queryset=SubmissionType.objects.filter(   date_open__lte=date.today(),
                                                                                            date_close__gte=date.today()  ))
                                                                      
MEDIA_UPLOAD_CHOICES = (
                                ('1',   'YouTube video'),
                                ('2',   'Photo upload'),
                        )

class SubmissionEntry2(forms.Form):
    """Individual or group submission, Age selection, Photo or YouTube"""
    submission_type = forms.ChoiceField(choices=SUBMISSION_GROUP_TYPE)
    age_category = forms.ModelChoiceField(queryset=AgeCategory.objects.all(), empty_label=None)
    media_upload_type = forms.ChoiceField(choices=MEDIA_UPLOAD_CHOICES)
    
class SubmissionEntry3(forms.Form):
    """Questions"""
    pass
    
class SubmissionEntry4(forms.Form):
    """Media upload"""
    pass
    
class SubmissionEntry5(forms.Form):
    """Group submission information"""
    pass
    
class SubmissionEntryConfirm(forms.Form):
    """Confirmation page"""
    pass
