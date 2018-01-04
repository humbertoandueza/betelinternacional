# -*- coding: utf-8 -*-

from django.views.decorators.gzip import gzip_page

from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import logout, login, authenticate
from django.views.generic import ListView, TemplateView

from django.views.generic import TemplateView, View

from django.template.context import RequestContext
from django.conf import settings

from django.contrib.auth.models import User
from .models import Users
from .forms import UsersModelForm, UsersUpdateModelForm
from django.contrib.auth.decorators import login_required


from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

# login

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm(request.FILES or None)
        return render(request, "aplicacion/aplicacion_login.html", { 'form': form })

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redirect
                url_next = request.GET.get('next')
                if url_next is not None:
                    return redirect('accounts:loguet')
                else:
                    return redirect('accounts:loguet')
            else:
                return HttpResponse("Inactive user.")
        else:
            return redirect('/login-error/')

        return render(request)


class login_error(View):
    def get(self, request):
        form = AuthenticationForm(request.FILES or None)
        return render(request, "aplicacion/aplicacion_loginError.html", { 'form': form })

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redirect
                url_next = request.GET.get('next')
                if url_next is not None:
                	return redirect('accounts:loguet')
                else:
                	return redirect('accounts:loguet')
            else:
            	return HttpResponse("Inactive user.")
        else:
        	return redirect('/login-error/')

        return render(request)

class UsersCreateView_alumno(CreateView):
    model = Users
    form_class = UsersModelForm
    template_name = 'aplicacion/form_create_alumno.html'
    success_url = reverse_lazy('accounts:Success_user_alumno')

class Estatus(UpdateView):
    model = Users
    form_class = UsersUpdateModelForm
    template_name = 'aplicacion/estatuschange.html'
    success_url = reverse_lazy('logout')

def Success_user_alumno(request):
    return render(request, 'aplicacion/succes_alumno.html')

def user_logueado(request):
    return render(request, 'aplicacion/paneladminnw.html')

class UsersCreateView_profesor(CreateView):
    model = Users
    form_class = UsersModelForm
    template_name = '.html'
    success_url = '/usuario_creado_profesor/'

def Success_user_profesor(request):
    return render(request, '.html')

#@login_required()
#@gzip_page
#def EliminarUser(request, pk):
#	x = get_object_or_404(Users, pk=pk)
#	x.delete()
#	return redirect('/lista/')