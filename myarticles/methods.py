# coding: utf-8
from django.core.urlresolvers import reverse
from corekit.methods import CoreModel


class Element(CoreModel):

    def get_absolute_url(self):
        return reverse('myarticles_element_detail', kwargs={'id': self.id})
