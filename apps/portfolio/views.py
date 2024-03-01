from django.shortcuts import render, redirect
from django.views.generic import (View, TemplateView)
# from .form import *
from django.contrib.auth import logout
from apps.utils import get_context

def portfolio_home(request):
    return render(request, 'portfolio/portfolio_home.html', {'current_page': 'portfolio_home','selected_language':get_context(request)})

def personal_projects(request):
    return render(request, 'portfolio/personal_projects.html', {'current_page': 'portfolio_home','selected_language':get_context(request)})

def professional_projects(request):
    return render(request, 'portfolio/professional_projects.html', {'current_page': 'portfolio_home','selected_language':get_context(request)})

def work_experience(request):
    return render(request, 'portfolio/work_experience.html', {'current_page': 'portfolio_home','selected_language':get_context(request)})
