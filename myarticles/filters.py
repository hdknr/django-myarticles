# coding: utf-8
import django_filters
from . import models


class ArticleFilter(django_filters.FilterSet):

    class Meta:
        model = models.Article
        exclude = []


class ElementFilter(django_filters.FilterSet):

    class Meta:
        model = models.Element
        exclude = []
