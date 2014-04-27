# Robogals Science Challenge
# Submissions for challenges and submission groups
#
# 2014 Robogals Software Team

from django.db import models
from django.core import validators
from django.utils import timezone

import os
from uuid import uuid4

class SubmissionType(models.Model):
    name = models.CharField(max_length=255, unique=False)
    
    resource_id = models.CharField('Resource ID', max_length=127, unique=True, help_text='Unique identifier for URL: /challenge/&lt;resource_id&gt;/. Further levels are not allowed.',
                                   validators=[
                                       validators.RegexValidator(r'^[\w-]+$', 'This value may contain only alphanumeric and _ or - characters.', 'invalid')
                                   ],)
                                   
    info_page = models.ForeignKey('scichal_cms.Component', help_text='Page containing information for this item. If unneeded, simply point to a blank page. The URL will be overridden with this item\'s resource ID as described above.')
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
    
class AgeCategory(models.Model):
    name = models.CharField(max_length=63, unique=False)
    age_min = models.PositiveIntegerField(default=0)
    age_max = models.PositiveIntegerField(default=18)
    
    class Meta:
        verbose_name = "age category"
        verbose_name_plural = "age categories"
    
    def __str__(self):
        return "{} ({}-{})".format(self.name, self.age_min, self.age_max)
        
class Submission(models.Model):
    # Based on http://stackoverflow.com/a/15141228
    def upload_rand_filename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            
            if (ext == filename):
                filename = '{}'.format(uuid4().hex)
            else:
                filename = '{}.{}'.format(uuid4().hex, ext)
            
            return os.path.join(path, filename)
        return wrapper
    
    title = models.CharField(max_length=255, unique=False, blank=True, null=True)
    
    submission_type = models.ForeignKey(SubmissionType)
    
    SUBMISSION_GROUP_TYPE = (
                              (0, 'Individual'),
                              (1, 'Standard Group'),
                              (2, 'School Class'),
                            )
    
    submission_group_type = models.IntegerField(choices=SUBMISSION_GROUP_TYPE, blank=True, null=True, default=0)

    
    users = models.ManyToManyField('scichal_user.SciChalUser', limit_choices_to={'is_active': True})
    age_category = models.ForeignKey(AgeCategory)
    
    body = models.TextField('Body HTML')
    
    youtube_id = models.CharField('YouTube ID', max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to=upload_rand_filename('submission_image'), blank=True, null=True)
    
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    def get_users(self):
        return ", ".join([user.get_full_name() for user in self.users.all()])
    get_users.short_description = 'User list'

class Question(models.Model):
    question = models.CharField(max_length=1023, unique=False)
    age_category = models.ForeignKey(AgeCategory, blank=True, null=True)
    submission_type = models.ForeignKey(SubmissionType)
    
    def __str__(self):
        return self.question