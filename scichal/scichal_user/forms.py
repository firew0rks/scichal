# Robogals Science Challenge
# Custom users
#
# 2014 Robogals Software Team

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import SciChalUser

# https://github.com/django/django/blob/master/django/contrib/auth/forms.py
class SciChalUserAddForm(forms.ModelForm):
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
    password = ReadOnlyPasswordHashField(label='Password',
                                         help_text="Raw passwords are not stored, so there is no way to see this user's password, but you can change the password using <a href='password/'>this form</a>.")

    class Meta:
        model = SciChalUser

    def clean_password(self):
        return self.initial['password']

