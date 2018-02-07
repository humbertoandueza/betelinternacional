#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(
            r'^loguet/$',
            login_required(user_logueado),
            name='loguet'
    ),

    # CREAR USUARIOS ALUMNOS
    url(
        r'^crear_usuario_alumno/$',
        UsersCreateView_alumno.as_view(),
        name='crear_usuario_alumno'
    ), 
    url(
        r'^succesfull/$',
        login_required(Estatus.as_view()),
        name='succesfull'
    ),
        url(
            r'^usuario_creado_alumno/$',
            login_required(Success_user_alumno),
            name='Success_user_alumno'
    ),

    url(
        r'^usuario_creado_profesor/$',
            login_required(Success_user_profesor),
            name='Success_user_profesor'
    ),
]
