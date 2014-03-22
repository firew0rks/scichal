# Robogals Science Challenge
# Custom basic CMS
#
# 2014 Robogals Software Team

from django.db import models
from django.core import validators

class Component(models.Model):
    resource_id = models.CharField('Resource ID', max_length=127, unique=True, help_text='Unique identifier for URLs. Separate different levels using the forward slash character (/). Must not start or end with slash. Use "home" for the home page.',
                                   validators=[
                                       validators.RegexValidator(r'^[\w/-]+$', 'This value may contain only alphanumeric and /, _ or - characters.', 'invalid')
                                   ],)
    enabled = models.BooleanField(default=True)
    
    title = models.CharField(max_length=255)
    title_display_head = models.BooleanField('Display title in <title>', default=True)
    menu_order = models.PositiveIntegerField(default=0, help_text='Positive integer for menu order. 0 = hidden from menu.')
    
    body = models.TextField('Body HTML')
    body_class = models.CharField(max_length=127, blank=True)
    
    template = models.CharField(max_length=127, blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-enabled', 'menu_order', 'resource_id']
        
    def __str__(self):
        return self.title