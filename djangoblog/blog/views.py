# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Blog, Category
from .forms import CommentForm

ARCHIVE_STRS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]


def index(request):
    # create the archive objects on the right side of the screen
    arch = Blog.objects.dates('posted', 'month', order='DESC')
    archives = {}

    for a in arch:
        year = str(a.year)
        month = a.month

        if year not in archives:
            archives[year] = []

        if month not in archives[year]:
            archives[year].append(month)


    return render(request, 'blog_index.html', {
        'nav': 'blog',
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5],
        'archives': sorted(archives.items(), reverse=True),
        'months': ARCHIVE_STRS,
    })


def view_post(request, slug, year, month, day):
    post = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    return render(request, 'view_post.html', {
        'nav': 'blog',
        'post': post,
        'form': form,
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'view_category.html', {
        'nav': 'blog',
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })


def view_archive(request, year, month):
    posts = []
    arch = Blog.objects.dates('posted', 'month', order='DESC')
    for a in arch:
        if year == a.year:
            if month == a.month:
                posts.append(a)

    header = ARCHIVE_STRS[month-1] + ' ' + str(year)

    return render(request, 'view_archive.html', {
        'nav': 'blog',
        'posts': posts,
        'header': header,
    })