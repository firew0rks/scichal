# Robogals Science Challenge
# Submissions for challenges and submission groups
#
# 2014 Robogals Software Team

from django.db import models
from django.core import validators
from django.utils import timezone

class SubmissionType(models.Model):
    name = models.CharField(max_length=255, unique=False)
    
    resource_id = models.CharField('Resource ID', max_length=127, unique=True, help_text='Unique identifier for URL: /challenge/&lt;resource_id&gt;/. Further levels are not allowed.',
                                   validators=[
                                       validators.RegexValidator(r'^[\w-]+$', 'This value may contain only alphanumeric and _ or - characters.', 'invalid')
                                   ],)
                                   
    info_page = models.ForeignKey('scichal_cms.Component', limit_choices_to={'enabled': True}, help_text='Page containing information for this item. If unneeded, simply point to a blank page. The URL will be overridden with this item\'s resource ID as described above.')
    info_page_visible = models.BooleanField(default=True)
    
    submission_view_template = models.CharField(max_length=127, blank=True)
    
    max_users = models.PositiveIntegerField(default=0, help_text='Maximum number of users per submission. 0 = unlimited.')
    
    allows_youtube = models.BooleanField(default=True)
    allows_images = models.BooleanField(default=True)
    
    date_open = models.DateField(default=timezone.now)
    date_close = models.DateField(default=timezone.now)
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Submission(models.Model):
    title = models.CharField(max_length=255, unique=False, blank=True, null=True)
    
    submission_type = models.ForeignKey(SubmissionType)
    
    users = models.ManyToManyField('scichal_user.SciChalUser', limit_choices_to={'is_active': True})
    
    body = models.TextField('Body HTML')
    
    youtube_id = models.CharField('YouTube ID', max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='submission_image', blank=True, null=True)
    
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title