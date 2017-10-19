# coding: utf-8
from django.core.urlresolvers import reverse
from mywords.models import Word
from corekit.methods import CoreModel
from . import signals


class Article(CoreModel):
    on_publish = signals.article_publish

    def update_links(self):
        if self.keywords:
            for i in self.keywords.split(','):
                i = i and i.strip()
                word, created = Word.objects.get_or_create(text=i)
                if word:
                    word.link_set.get_or_create(
                        content_type=self.contenttype(), object_id=self.id)

    def publish(self):
        self.on_publish.send(self.__class__, instance=self)


class Element(CoreModel):

    def get_absolute_url(self):
        return reverse('myarticles_element_detail', kwargs={'id': self.id})
