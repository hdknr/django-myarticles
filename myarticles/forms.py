# coding: utf-8
from django import forms
from mylinks.models import Page
from . import models


class ArticleForm(forms.ModelForm):

    class Meta:
        model = models.Article
        fields = ['title', 'keywords', 'description', 'catch', ]


class SectionForm(forms.ModelForm):

    class Meta:
        model = models.Section
        exclude = ['article', ]



class SubsectionForm(forms.ModelForm):

    class Meta:
        model = models.Subsection
        exclude = ['article', ]


class TextForm(forms.ModelForm):

    class Meta:
        model = models.Text
        exclude = ['article', ]


class TextForm(forms.ModelForm):

    class Meta:
        model = models.Text
        exclude = ['article', ]


class ImageForm(forms.ModelForm):

    class Meta:
        model = models.Image
        exclude = ['article', ]


class LinkForm(forms.ModelForm):
    url = forms.URLField(required=True)

    class Meta:
        model = models.Link
        exclude = ['article', 'page', ]

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        instance = kwargs.get('instance', {})
        if instance and instance.page:
            initial['url'] = initial.get('url', None) or \
                instance.page.url
            kwargs['initial'] = initial
        super(LinkForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        instance = super(LinkForm, self).save(*args, **kwargs)
        if 'url' in self.changed_data:
            page, created = Page.objects.get_or_create(
                url=self.cleaned_data['url'])
            page.update_content()
            instance.page = page
            instance.save()

        return instance


class QuoteForm(forms.ModelForm):

    class Meta:
        model = models.Quote
        exclude = ['article', ]


class LocationForm(forms.ModelForm):

    class Meta:
        model = models.Location
        exclude = ['article', ]
