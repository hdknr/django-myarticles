# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from corekit import utils, methods
from .. import models, forms
register = template.Library()


@register.simple_tag(takes_context=False)
def render_element(
        element, request=None, **kwargs):
    template_name = 'articles/element/{1}.{2}/{0}.html'.format(
        'detail', *element.contenttype().natural_key())
    return utils.render_by(
        template_name, instance=element, request=request, **kwargs)


@register.simple_tag(takes_context=False)
def article_meta(
        instance, request=None, **kwargs):
    template_name = 'articles/article/meta/detail.html'
    return utils.render_by(
        template_name, instance=instance, request=request, **kwargs)


@register.simple_tag
def elements():
    return [{'meta': i._meta, 'type': ContentType.objects.get_for_model(i)}
            for i in models.Element.__subclasses__()]

@register.simple_tag
def element_insert_form(prefix='insert-element'):
    return forms.ElementInsertForm(prefix=prefix)
