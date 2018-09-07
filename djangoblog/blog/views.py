# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Blog, Category


def index(request):
    return render(request, 'blog_index.html', {
        'nav': 'blog',
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })


def view_post(request, slug):
    return render(request, 'view_post.html', {
        'nav': 'blog',
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'view_category.html', {
        'nav': 'blog',
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

