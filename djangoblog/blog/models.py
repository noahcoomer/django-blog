# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.dateparse import parse_datetime
import datetime


# Blog Posts Model
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    body = models.TextField()  # type: object
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    # this field can be changed to .manyToMany() to support multiple categories
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)
    author = models.ForeignKey('blog.Author', on_delete=models.CASCADE)
    length = models.IntegerField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        url = reverse('view_post', kwargs={
            'slug': self.slug,
            'year': self.posted.year,
            'month': self.posted.month,
            'day': self.posted.day
        })
        return url


# Category Query Model
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        url = reverse('view_category', kwargs={'slug': self.slug})
        return url


# Author Information Model
class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % self.name


# Base Comment Model
class Comment(models.Model):
    post = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=40)
    text = models.TextField()
    created_date = models.DateTimeField(db_index=True, auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


# Base Audio File Model
class AudioFile(models.Model):
    specifications = models.FileField(upload_to='router_specifications')

