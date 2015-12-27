from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

def index(request, question_id):
    posts = Post.objects.filter(link=question_id)
    type = question_id
    return render(request, 'home/home.html', {'posts': posts,'type':type})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
