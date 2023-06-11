from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.exceptions import PermissionDenied
from blog.models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    context_object_name = "post"

    def get_object(self):
        """
        直接記事URLにアクセスしても,公開フラグがFalseの場合 Permission Deniedを返す.
        """
        post = super().get_object()
        if post.is_published:
            return post
        else:
            raise PermissionDenied
