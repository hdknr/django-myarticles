# coding: utf-8
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType
from corekit.methods import CoreModel


class Graph(object):

    def __init__(self, element, parent):
        self.parent = parent
        self.element = element.instance
        self.children = []

    @property
    def container_level(self):
        return self.element.container_level

    def add_child(self, element):
        new = Graph(element, self)
        self.children.append(new)
        return self

    def add_holder(self, element):
        new = Graph(element, self)
        self.children.append(new)
        return new

    def add(self, element):
        if not element.is_container:
            return self.add_child(element)

        current = self
        if current.parent:
            if element.container_level == current.container_level:
                current = current.parent
            elif not current.parent.parent:
                current = current.parent
            elif element.container_level < current.container_level:
                current = current.parent.parent
        current = current.add_holder(element)
        return current

    def render_content(self):
        return self.element.render_content(graph=self)


class Article(CoreModel):

    @property
    def graph(self):
        root = Graph(self, None)
        current = root

        for e in self.element_set.all():
            current = current.add(e)

        return root

    def render_content(self):
        return render_to_string(
            'articles/article/content.html',
            context=dict(graph=self.graph))

    def check_perm(self, user, code='articles.change_article'):
        # subclass model MUST implement has_perm method
        return self.instance.has_perm(user, code)


class Element(CoreModel):

    def get_absolute_url(self):
        return reverse('myarticles_element_detail', kwargs={'id': self.id})

    @property
    def element_name(self):
        '''element name'''
        return self.instance._meta.model_name

    @property
    def element_fullname(self):
        '''app_label.model_name '''
        return ".".join(self.contenttype().natural_key())

    @property
    def is_container(self):
        return self.element_name in ['section', 'subsection']

    @property
    def container_level(self):
        try:
            return ['section', 'subsection'].index(self.element_name) + 2
        except:
            return ''

    def render_content(self, **kwargs):
        return render_to_string(
            'articles/element/{}/content.html'.format(self.element_fullname),
            context=kwargs)
