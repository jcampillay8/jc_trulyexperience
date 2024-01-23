from django.shortcuts import render, redirect
from django.views.generic import (View, TemplateView)
# from .form import *
from django.contrib.auth import logout
from apps.utils import get_context


def portfolio_home(request):
    return render(request, 'portfolio/portfolio_home.html', {'current_page': 'portfolio_home','selected_language':get_context(request)})