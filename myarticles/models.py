# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from ordered_model.models import OrderedModel
from . import methods, defs


class Article(defs.Article):

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')


class Element(OrderedModel, methods.Element):
    article = models.ForeignKey(Article)

    order_with_respect_to = 'article'
    order_class_path = 'myarticles.models.Element'

    class Meta:
        verbose_name = _('Element')
        verbose_name_plural = _('Elements')
        ordering = ['article', 'order', ]


class Section(Element):

    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')


class Subsection(Element):

    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Subsection')
        verbose_name_plural = _('Subsections')


class Text(Element):

    texts = models.TextField()

    class Meta:
        verbose_name = _('Text')
        verbose_name_plural = _('Texts')


class Image(Element):

    image_url = models.URLField()

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


class Link(Element):

    url = models.URLField()
    image_url = models.URLField(
        null=True, default=None, blank=True)

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')


class Quote(Element):

    url = models.URLField()
    texts = models.TextField()
    source = models.TextField()

    class Meta:
        verbose_name = _('Quote')
        verbose_name_plural = _('Quotes')


class Location(Element):

    address = models.TextField()

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')
