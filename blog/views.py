from django.shortcuts import render
from .models import Post

def blog(request):
    _all_posts = Post.objects.all()
    return render(request, 'blog/blog.html', { 'posteos': _all_posts})