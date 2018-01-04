#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils import timezone
from .models import *

class UserManager(BaseUserManager):
	def create_user(self,ci,password=None ,**kwargs):
		if not ci:
			raise ValueError('Users must have invalid ci.')

		account = self.model(
			ci=self.model.normalize_username(ci)
		)

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self,ci,password,**kwargs):
		account = self.create_user(ci,password,**kwargs)

		account.is_superuser = True
		account.is_staff = True
		account.save()

		return account

class Users(AbstractBaseUser, PermissionsMixin):
	ci = models.CharField(_('Cedula'),max_length=60,unique=True,primary_key=True)
	username = models.CharField(_('Username'),max_length=40,null=True,unique=True)
	email = models.EmailField(_('Email'))
	first_name = models.CharField(_('first name'), max_length=40)
	last_name = models.CharField(_('last name'), max_length=40)

	is_active = models.BooleanField(_('Active'), default=True)
	is_staff = models.BooleanField(_('Staff Status'), default=False)
	is_superuser = models.BooleanField(_('Superuser Status'), default=False)
	is_alumno = models.BooleanField(_('Alumno Status'), default=False)
	is_profesor = models.BooleanField(_('Profesor Status'), default=False)
	is_inscripcion = models.BooleanField(_('Inscripcion Status'), default=False)


	date_joined = models.DateTimeField(_('Sate Joined'), default=timezone.now)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELD = ['email']

	def __str__(self): #si es python 2.7 es def __unicode__(self):
		return '{}, {}, {}' .format(self.username, self.first_name, self.last_name)

	def get_full_name(self):
		return '' .join([self.first_name, self.last_name]).encode('utf-8').strip()

	def get_short_name(self):
		return self.first_name

	def save(self, *args, **kwargs):
		if self.username:
			self.username = self.ci
			super(Users, self).save(*args, **kwargs)