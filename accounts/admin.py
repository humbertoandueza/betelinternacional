from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_superuser',
        'is_active',
        'is_alumno',
        'is_profesor',
        'is_inscripcion',
        'groups',
    )

    search_fields = (
        'username',
        'ci',
        'first_name',
        'last_name',
        'email',
    )

    ordering = (
        'ci',
    )

    filter_horizontal = (
        'groups',
    )

    fieldsets = (
        (None,
            {'fields': (
                'ci',
                'password',
            )}), (_('Personal info'),
                {'fields': (
                    'ci',
                    'first_name',
                    'last_name',
                    'email',
                )}), (_('Permissions'),
                    {'fields': (
                        'is_active',
                        'is_staff',
                        'is_superuser',
                        'is_alumno',
                        'is_profesor',
                        'is_inscripcion',
                        'groups',
                    )}), (_('Important dates'),
                        {'fields': (
                            'last_login',
                            'date_joined',
                        )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'ci',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2'
            ),
        }),
    )

    class Meta:
    	model = Users
admin.site.register(Users, UserAdmin)