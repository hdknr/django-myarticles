# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    keywords = models.TextField(null=True, default=None, blank=True)
    description = models.TextField(null=True, default=None, blank=True)

    html = models.TextField(null=True, blank=True, default=None)

    class Meta:
        abstract = True
