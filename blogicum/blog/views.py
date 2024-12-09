from lib2to3.fixes.fix_input import context
from pydoc import locate

from django.shortcuts import render, get_object_or_404
from unicodedata import category

from. models import Post, Category
from datetime import datetime

def posts():
    return Post.objects.select_related(
        'location',
        'author',
        'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.today()
    )


def index(request):
    template_name = 'blog/index.html'
    context = {'post_list': posts()[:5]}
    return render(request, template_name, context)

def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug = category_slug,
        is_published=True
    )
    context = {
        'category': category,
        'post_list': posts().filter(category=category)
    }
    template_name = 'blog/category.html'
    return render(request, template_name, context)

def post_detail(request, id):
    post = get_object_or_404(posts(), id=id)
    context = {
        'post': post
    }
    template_name = 'blog/detail.html'
    return render(request, template_name, context)
