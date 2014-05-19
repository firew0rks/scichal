# Robogals Science Challenge
# Submissions for challenges and submission groups
#
# 2014 Robogals Software Team

from django import forms

from datetime import datetime

from .models import SubmissionType

class SubmissionEntry1(forms.Form):
    """Choose a challenge to begin with."""
    # available_challenges = forms.ChoiceField(SubmissionType.objects.filter( date_open__lte=datetime.now(),
                                                                            # date_close__gte=datetime.now(),
                                                                          # ))
    available_challenges = forms.ChoiceField(SubmissionType.objects.all())

SUBMISSION_GROUP_CHOICES = (
                                ('1',   'Individual'),
                                ('2',   'Group (Standard)'),
                                ('3',   'Group (School class)'),
                            )                                                                          
MEDIA_UPLOAD_CHOICES = (
                                ('1',   'YouTube video'),
                                ('2',   'Photo upload'),
                        )

class SubmissionEntry2(forms.Form):
    """Individual or group submission, Photo or YouTube"""
    submission_group = forms.ChoiceField(choices=SUBMISSION_GROUP_CHOICES)
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
