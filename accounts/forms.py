#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from .formsDate import *

class UsersModelForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class':'form-control', 'autocomplete':'off'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirme Contraseña', 'class':'form-control', 'autocomplete':'off'}))
    class Meta:
        model = Users
        exclude = ('created_at', 'updated_at', 'user_permissions',
            'last_login', 'is_active', 'date_joined', 'password')

        widgets = {
            'ci': forms.NumberInput(attrs={'placeholder': 'Cedula', 'class':'form-control', 'autocomplete':'off','oninput':'maxLengthCheck(this)','maxlength':'8','onKeyUp':'this.value=this.value.toUpperCase();'}),

            #'ci': forms.TextInput(attrs={'placeholder': 'Cedula', 'class':'form-control', 'autocomplete':'off','oninput':'maxLengthCheck(this)','maxlength':8,'onKeyUp':'this.value=this.value.toUpperCase();'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido', 'class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class':'form-control', 'autocomplete':'off','type':'password'}),    
            'birthday': DateInput(format = '%Y-%m-%d'),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'is_alumno': forms.CheckboxInput(attrs={'checked':'checked'}),
            'is_staff': forms.CheckboxInput(attrs={'checked':'checked'}),
            'is_superuser': forms.CheckboxInput(attrs={'checked':'checked'}),
            'is_inscripcion': forms.CheckboxInput(attrs={'checked':'checked'}),
            'is_profesor': forms.CheckboxInput(attrs={'checked':'checked'}),

            'username': forms.TextInput(attrs={'value':'cedula'}),
            'id_usuario': forms.TextInput(attrs={'value':'1'}),

        }


class UsersUpdateModelForm(UserChangeForm):

    class Meta:
        model = Users
        exclude = ('created_at', 'updated_at', 'user_permissions',
            'last_login', 'is_active', 'date_joined','is_alumno'
            ,'is_profesor','username','id_usuario','email',
            'last_name','first_name','ci','password1','birthday','is_staff')
        widgets = {
            'is_inscripcion': forms.CheckboxInput(),
        }
