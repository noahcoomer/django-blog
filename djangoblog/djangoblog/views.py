from __future__ import unicode_literals

from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def legal(request):
    return render(request, 'legal.html', {})


def terms(request):
    return render(request, '', {})