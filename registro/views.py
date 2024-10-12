from django.shortcuts import render
from django.contrib.auth.models import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

# Create your views here.

class signupView(CreateView):
  template_name = "registration/signup.html"
  form_class = UserCreationForm
  success_url = reverse_lazy("login")

class LogoutView(TemplateView):
  template_name = "logout.html"