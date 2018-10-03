from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(db_index=True, auto_now_add=True)