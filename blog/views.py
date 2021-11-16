from django.shortcuts import get_object_or_404, render
from .models import Category, Post

def blog(request):
    _all_posts = Post.objects.all()
    return render(request, 'blog/blog.html', { 'posteos': _all_posts})

#def category(request, category_id ):
    # Me traigo el objeto category con el id del front
#    category = get_object_or_404(Category, id=category_id ) # Category.objects.get(id=category_id)
    # Me traigo los post que tengan esta categoria
#    _all_posts = Post.objects.filter(categories=category)
#    return render(request, 'blog/category.html', {'categoria': category, 'posteos': _all_posts })


def category(request, category_id ):
    category = get_object_or_404(Category, id=category_id )
    return render(request, 'blog/category.html', { 'categoria': category })
