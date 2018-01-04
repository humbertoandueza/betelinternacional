#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
