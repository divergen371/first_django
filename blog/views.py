from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    context_object_name = "posts"


class PostDetail(DetailView):
    nodel = Post
    context_object_name = "post"
