# coding: utf-8
from factory import DjangoModelFactory as ModelFactory, Sequence
from django.contrib.auth.models import User
from . import models


class UserFactory(ModelFactory):

    class Meta:
        model = User

    username = Sequence(lambda n: "User{}".format(n))

    @classmethod
    def get_or_create(cls):
        if not cls._meta.model.objects.exists():
            cls.create_random(count=1)
        return cls._meta.model.objects.first()

    @classmethod
    def create_random(cls, count=100):
        return cls.create_batch(count)


class ArticleFactory(ModelFactory):

    class Meta:
        model = models.Article

    title = Sequence(lambda n: "Article {}".format(n))

    @classmethod
    def get_or_create(cls):
        if not cls._meta.model.objects.exists():
            cls.create_random(count=1)
        return cls._meta.model.objects.first()

    @classmethod
    def create_random(cls, count=100):
        author = UserFactory.get_or_create()
        return cls.create_batch(count, author=author)


class ElementFactory(ModelFactory):
    class Meta:
        model = models.Element

    @classmethod
    def create_random(cls, count=100, **kwargs):
        kwargs['article'] = kwargs.get('article', None) or \
            ArticleFactory.get_or_create()
        return cls.create_batch(count, **kwargs)


class SectionFactory(ElementFactory):
    class Meta:
        model = models.Section

    title = Sequence(lambda n: "Section {}".format(n))


class SubsectionFactory(ElementFactory):
    class Meta:
        model = models.Subsection

    title = Sequence(lambda n: "Subsection {}".format(n))


class TextFactory(ElementFactory):
    class Meta:
        model = models.Text

    texts = Sequence(lambda n: "your texts {}".format(n))


class ImageFactory(ElementFactory):
    class Meta:
        model = models.Image

    image_url = Sequence(lambda n: "http://yoursite.com/images/{0}.png".format(n))


class LinkFactory(ElementFactory):
    class Meta:
        model = models.Link

    url = Sequence(lambda n: "http://yoursite.com/link/{0}".format(n))
    image_url = Sequence(lambda n: "http://yoursite.com/link/images/{0}.png".format(n))



class QuoteFactory(ElementFactory):
    class Meta:
        model = models.Quote

    url = Sequence(lambda n: "http://yoursite.com/quote/{0}".format(n))
    texts = Sequence(lambda n: "quoted texts {}".format(n))
    source = Sequence(lambda n: "quoted from {}".format(n))


class LocationFactory(ElementFactory):
    class Meta:
        model = models.Location

    address = Sequence(lambda n: "location address{}".format(n))
