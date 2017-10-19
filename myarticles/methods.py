# coding: utf-8
from django.core.urlresolvers import reverse
from mywords.models import Word
from corekit.methods import CoreModel


class Article(CoreModel):

    def update_links(self):
        if self.keywords:
            for i in self.keywords.split(','):
                word, created = Word.objects.get_or_create(text=i)
                if word:
                    word.link_set.get_or_create(
                        content_type=self.contenttype(), object_id=self.id)


class Element(CoreModel):

    def get_absolute_url(self):
        return reverse('myarticles_element_detail', kwargs={'id': self.id})
