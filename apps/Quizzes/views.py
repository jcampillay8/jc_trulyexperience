from django import forms
import django
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from apps.Quizzes.models import Post, UserQuestionValue, Question
from apps.Quizzes.forms import PostForm
from apps.Quizzes.gcp_trainer_app import app
from apps.utils import get_context



def quiz_index(request):
    return redirect('quiz_post')

@login_required(login_url='login')
def createQuiz(request):
    request.session['language'] = request.POST.get('language', 'English')
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES)    
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            # post.autor = request.user.username
            post.save()
            return redirect('quiz_index')
    else:
        form = PostForm()
        return render(request, 'Quizzes/quiz_creation.html', {'form': form})


@login_required(login_url='login')
def seeQuiz(request, pk=None):
    if pk is not None:
        post = get_object_or_404(Post, id=pk)
        tieneLike = request.user in post.likes.all()
    else:
        post = None
        tieneLike = False

    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    num_pagina = request.GET.get('page')
    pagina_actual = paginator.get_page(num_pagina)

    return render(request, 'Quizzes/quiz_post.html', {'post':post, 'likes': post.cantidad_likes() if post else 0, 'tiene_like': tieneLike,'current_page': 'Quizzes', 'selected_language':get_context(request), 'posts': pagina_actual})

@login_required(login_url='login')
def updateQuiz(request, pk):
    # post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, id=pk)
    if request.user == post.autor:
        if request.method == 'POST':
            form =PostForm(request.POST, request.FILES, instance=post)    
            if form.is_valid():
                post.save()
                return redirect('quiz_index')
        else:
            form = PostForm(instance=post)
            return render(request, 'Quizzes/quiz_creation.html', {'form': form})
    else:
        return redirect(f'/quiz_post/{post.id}')

@login_required(login_url='login')
def deleteQuiz(request, pk):
    # post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, id=pk)
    if post.autor == request.user:
        if request.method == 'POST':
            post.delete()
            return redirect('index')
        
        return render(request, 'Quizzes/quiz_delete.html', {'post':post})
    else:
        return redirect(f'/post/{post.id}')

@login_required(login_url='login')
def darLike(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('/quiz_post/'+str(post.id))
    else:
        raise Http404()




@login_required(login_url='login')
def dash_view(request, pk):

    request.session['language'] = request.POST.get('language', 'English')
    post = get_object_or_404(Post, id=pk)
    
    request.session['username'] = request.user.username

    context = {
        'post': post,
        'username': request.user.username  
    }

    if pk == 8:
        return render(request, 'Quizzes/quiz_gcp_digital_leader.html', {'post': post,'username': request.user.username, 'current_page': 'Quizzes','selected_language':get_context(request) })
    else:
        return render(request, 'Quizzes/quiz_no_disponible.html', context)
    


@login_required(login_url='login')
def test(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'Quizzes/test.html',{'post':post})


