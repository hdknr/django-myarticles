# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse
from corekit import utils, methods
register = template.Library()


@register.simple_tag(takes_context=False)
def render_element(
        element, request=None, **kwargs):
    template_name = 'articles/element/{1}.{2}/{0}.html'.format(
        'detail', *element.contenttype().natural_key())
    return utils.render_by(
        template_name, instance=element, request=request, **kwargs)
