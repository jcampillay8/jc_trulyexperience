from django.shortcuts import render, redirect
from django.views.generic import (View, TemplateView)
from .form import *
from django.contrib.auth import logout
from apps.utils import get_context


def about_me(request):
    # context = {'blogs': BlogModel.objects.all(),'selected_language':get_context(request)}
    return render(request, 'blog/about_me.html', {'about_me': BlogModel.objects.all(),'current_page': 'blog','selected_language':get_context(request)})

def blog(request):
    context = {'blogs': BlogModel.objects.all(),'selected_language':get_context(request)}
    return render(request, 'blog/blog.html', {'blogs': BlogModel.objects.all(),'current_page': 'blog','selected_language':get_context(request), 'current_page':'blog'})


def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog/blog_detail.html', context)


def see_blog(request):
    context = {'current_page':'blog'}

    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'blog/see_blog.html', context)


def add_blog(request):
    context = {'form': BlogForm,'current_page':'blog'}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(blog_obj)
            return redirect('/add-blog/')
    except Exception as e:
        print(e)

    return render(request, 'blog/add_blog.html', context)


def blog_update(request, slug):
    context = {}
    try:

        blog_obj = BlogModel.objects.get(slug=slug)

        if blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'blog/update_blog.html', context)


def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-blog/')



