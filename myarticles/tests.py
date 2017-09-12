# coding: utf-8
from django.test import TestCase
from . import factories


class ArticleTestCase(TestCase):

    def test_order(self):
        ''' ordered model test

        - https://github.com/bfirsh/django-ordered-model
        '''
        articles = factories.ArticleFactory.create_random(count=2)
        factories.SectionFactory.create_random(count=10, article=articles[0])
        factories.SectionFactory.create_random(count=10, article=articles[1])

        articles[0].element_set.last().top()    # last item to the 'top'
        ids0 = [(i.id, i.order) for i in articles[0].element_set.all()]
        ids1 = [(i.id, i.order) for i in articles[1].element_set.all()]
        self.assertTrue(ids0[0] > ids0[-1])
        self.assertTrue(ids1[0] < ids1[-1])
        self.assertEqual(sum([ids0[0][1], ids0[0][1]]), 0)  # 'order' is '0'

    def test_mixorder(self):
        ''' sub class models in order
        '''
        article = factories.ArticleFactory.create_random(count=1)[0]
        fs = [
            factories.SectionFactory,
            factories.SubsectionFactory,
            factories.TextFactory,
            factories.ImageFactory,
            factories.LinkFactory,
            factories.QuoteFactory,
            factories.LocationFactory, ]
        for f in fs:
            f.create_random(count=1, article=article)

        last = article.element_set.last()
        self.assertEqual(last.instance._meta.model, fs[-1]._meta.model)
        last.top()
        self.assertEqual(
            article.element_set.first().instance._meta.model,
            fs[-1]._meta.model)


class FormTestCase(TestCase):

    def test_create(self):
        class_name = [
            'myarticles.forms.SectionForm',
            'myarticles.forms.SubsectionForm',
            'myarticles.forms.TextForm',
            'myarticles.forms.ImageForm',
            'myarticles.forms.LinkForm',
            'myarticles.forms.QuoteForm',
            'myarticles.forms.LocationForm',
        ]
        from django.utils.module_loading import import_string
        for name in class_name:
            form = import_string(name)
            print(form)
