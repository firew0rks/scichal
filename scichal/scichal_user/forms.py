# Robogals Science Challenge
# Custom users
#
# 2014 Robogals Software Team

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms.extras.widgets import SelectDateWidget

#import datetime

from .models import SciChalUser
from .widgets import MonthYearWidget

# https://github.com/django/django/blob/master/django/contrib/auth/forms.py
class SciChalUserAddForm(forms.ModelForm):
    "User addition form used internally."
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = SciChalUser
        fields = (
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                  )
                  
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(SciChalUserAddForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class SciChalUserChangeForm(forms.ModelForm):
    "User change form used internally."
    
    password = ReadOnlyPasswordHashField(label='Password',
                                         help_text="Raw passwords are not stored, so there is no way to see this user's password, but you can change the password using <a href='password/'>this form</a>.")

    class Meta:
        model = SciChalUser

    def clean_password(self):
        return self.initial['password']

class SciChalUserAccountForm(forms.ModelForm):
    "User account edit form used publically."

    class Meta:
        model = SciChalUser
        fields = (
                    'email',
                    'phone',
                    'location_address',
                    'location_state',
                    'location_postcode',
                    'mentor_first_name',
                    'mentor_last_name',
                    'mentor_email', 
                    'mentor_phone',
                    'mentor_relationship',
                    'school_name',
                    'school_address',
                    'school_state',
                    'school_postcode',
                  )
        
        
    def clean(self):
        data = self.cleaned_data
        error_messages = []
        
        field_desc = {
                    'email':            "Your email",
                    'phone':            "Your phone number",
                    'location_address': "Your address",
                    'location_state':   "Your state/territory",
                    'location_postcode':"Your postcode",
                    'mentor_first_name':"Your mentor's first name",
                    'mentor_last_name': "Your mentor's last name",
                    'mentor_email':     "Your mentor's email",
                    'mentor_phone':     "Your mentor's phone number",
                    'mentor_relationship':  "Your mentor's relationship with you",
                    'school_name':      "Your school's name",
                    'school_address':   "Your school's address",
                    'school_state':     "Your school's state/territory",
                    'school_postcode':  "Your school's postcode",
                     }
        
        for field in sorted(data):
            if (data[field] == None):
                error_messages.append("{} cannot be blank.".format(field_desc[field]))
            elif (len(data[field]) == 0):
                error_messages.append("{} cannot be blank.".format(field_desc[field]))
        
        if error_messages:
            raise forms.ValidationError("\n".join(error_messages))
        
        return data

class SciChalUserAccountRegisterForm(forms.ModelForm):
    "User account registration form used publically."
    
    password = forms.CharField(widget=forms.PasswordInput)
    dob = forms.DateField(widget=MonthYearWidget)
    
    class Meta:
        model = SciChalUser
        
        fields = (
                    'email',
                    'phone',
                    'location_address',
                    'location_state',
                    'location_postcode',
                    'mentor_first_name',
                    'mentor_last_name',
                    'mentor_email', 
                    'mentor_phone',
                    'mentor_relationship',
                    'school_name',
                    'school_address',
                    'school_state',
                    'school_postcode',
                    'username',
                    'password',
                    'first_name',
                    'last_name',
                    'referral_statement',
                    'dob'
                )
        
    def clean(self):
        data = self.cleaned_data
        error_messages = []
        
        field_desc = {
                    'email':            "Your email",
                    'phone':            "Your phone number",
                    'location_address': "Your address",
                    'location_state':   "Your state/territory",
                    'location_postcode':"Your postcode",
                    'mentor_first_name':"Your mentor's first name",
                    'mentor_last_name': "Your mentor's last name",
                    'mentor_email':     "Your mentor's email",
                    'mentor_phone':     "Your mentor's phone number",
                    'mentor_relationship':  "Your mentor's relationship with you",
                    'school_name':      "Your school's name",
                    'school_address':   "Your school's address",
                    'school_state':     "Your school's state/territory",
                    'school_postcode':  "Your school's postcode",
                    'username':         "Your username",
                    'password':         "Your password",
                    'first_name':       "Your first name",
                    'last_name':        "Your last name",
                    'referral_statement':   "Your referral statement"
                    }
        
        for field in sorted(data):
            if (field != "dob"):
                if (data[field] == None):
                    error_messages.append("{} cannot be blank.".format(field_desc[field]))
                elif (len(data[field]) == 0):
                    error_messages.append("{} cannot be blank.".format(field_desc[field]))
            
        if error_messages:
            raise forms.ValidationError("\n".join(error_messages))
        
        return data
    
    
    
    def save(self, commit=True):
        user = super(SciChalUserAccountRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
        return user