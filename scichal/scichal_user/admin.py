# Robogals Science Challenge
# Custom users
#
# 2014 Robogals Software Team

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SciChalUserAddForm, SciChalUserChangeForm
from .models import SciChalUser

class SciChalUserAdmin(UserAdmin):
    # Form to implement special password field and two-stage user-add form
    form = SciChalUserChangeForm
    add_form = SciChalUserAddForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                        'username',
                        'first_name',
                        'last_name',
                        'email',
                        'password1',
                        'password2',
                      )
               }
        ),
    )
    
    list_display = ('username', 'last_name', 'first_name', 'email', 'location_state', 'location_postcode',)
    search_fields = ('username', 'last_name', 'first_name', 'email',)
    ordering = ('last_name', 'first_name', 'username',)
    
    list_filter = ('location_state', 'is_superuser', 'is_active',)
    
    fieldsets = [
        ('User credentials',     {'fields': ['username', 'password']}),
        ('Personal information', {'fields': ['first_name', 'last_name', 'email', 'phone', 'dob', 'location_address', 'location_state', 'location_postcode']}),
        ('Mentor',               {'fields': ['mentor_first_name', 'mentor_last_name', 'mentor_email', 'mentor_phone',  'mentor_relationship'], 'classes': ['collapse']}),
        ('School',               {'fields': ['school_name', 'school_address', 'school_state', 'school_postcode'], 'classes': ['collapse']}),
        ('Referrals',            {'fields': ['referral_statement'], 'classes': ['collapse']}),
        ('Advanced',             {'fields': ['date_joined', 'is_active', 'is_superuser'], 'classes': ['collapse']}),
    ]
    
admin.site.register(SciChalUser, SciChalUserAdmin)