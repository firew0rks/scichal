# Robogals Science Challenge
# Custom users
#
# 2014 Robogals Software Team

from django.db import models
from django.core import validators
from django.utils import timezone

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

import string
import random

class SciChalUserManager(BaseUserManager):
    def _create_user(self, username, email, password,
                     is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True,
                                 **extra_fields)

class SciChalUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(('Username'), max_length=63, unique=True, help_text='Required. 63 characters or fewer. Letters, digits and ./-/_ only.',
                    validators=[
                        validators.RegexValidator(r'^[\w.-]+$', 'Enter a valid username.', 'invalid')
                    ])
    
    first_name = models.CharField('First name', max_length=255, null=False, blank=False)
    last_name = models.CharField('Last name', max_length=255, null=False, blank=False)
    
    email = models.EmailField('Email address', unique=True, error_messages={'required': 'Your email is required.'})
    
    phone = models.CharField('Phone number', max_length=15, blank=True, null=True,
                    validators=[
                        validators.RegexValidator(r'^\+{0,1}[0-9]+$','Enter a valid phone number.','invalid')
                    ])
    
    dob = models.DateField('Date of Birth', blank=True, null=True)
    
    LOCATION_STATE_CHOICES = (
                              ('ACT', 'Australian Capital Territory'),
                              ('NSW', 'New South Wales'),
                              ('NT', 'Northern Territory'),
                              ('QLD', 'Queensland'),
                              ('SA', 'South Australia'),
                              ('TAS', 'Tasmania'),
                              ('VIC', 'Victoria'),
                              ('WA', 'Western Australia'),
                             )
    
    location_address = models.TextField('Address', blank=True, null=True)
    location_state = models.CharField('State', max_length=3, blank=True, null=True, choices=LOCATION_STATE_CHOICES)
    location_postcode = models.CharField('Postcode', max_length=4, blank=True, null=True,
                    validators=[
                        validators.RegexValidator(r'^[0-9]{4}$','Enter a valid postcode.','invalid')
                    ])

    school_name = models.CharField('School name', max_length=255, blank=True, null=True)
    school_address = models.TextField('School address', blank=True, null=True)
    school_state = models.CharField('School state', max_length=3, blank=True, null=True, choices=LOCATION_STATE_CHOICES)
    school_postcode = models.CharField('School postcode', max_length=4, blank=True, null=True,
                    validators=[
                        validators.RegexValidator(r'^[0-9]{4}$','Enter a valid postcode.','invalid')
                    ])
    
    mentor_first_name = models.CharField('Mentor first name', max_length=255, blank=True, null=True)
    mentor_last_name = models.CharField('Mentor last name', max_length=255, blank=True, null=True)
    mentor_email = models.EmailField('Mentor email address', blank=True, null=True)
    mentor_phone = models.CharField('Mentor phone number', max_length=15, blank=True, null=True,
                    validators=[
                        validators.RegexValidator(r'^\+{0,1}[0-9]+$','Enter a valid phone number.','invalid')
                    ])
    mentor_relationship = models.CharField('Mentor relationship', max_length=255, blank=True, null=True)
    
    referral_statement = models.TextField('Referral statement', blank=True, null=True)
    
    is_active = models.BooleanField('Active', default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('Date joined', default=timezone.now)
    
    # http://stackoverflow.com/a/2257449
    def generate_pin():
        return ''.join(random.choice(string.digits) for _ in range(6))
    
    pin = models.CharField('PIN', max_length=6, blank=True, null=True, default=generate_pin,
                    validators=[
                        validators.RegexValidator(r'^[0-9]{6}$','Enter a valid PIN.','invalid')
                    ])
    
    objects = SciChalUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
    
    def is_staff(self):
        return self.is_superuser