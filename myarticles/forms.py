# coding: utf-8
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from mylinks.models import Page
from mymedia.models import Album
from . import models


class ArticleForm(forms.ModelForm):

    class Meta:
        model = models.Article
        fields = ['title', 'keywords', 'description', 'catch', ]
        widgets = {'catch': forms.HiddenInput, }


class ElementForm(object):

    @classmethod
    def for_model(cls, model_class):
        for c in cls.__subclasses__():
            if c.Meta.model == model_class:
                return c


class SectionForm(ElementForm, forms.ModelForm):

    class Meta:
        model = models.Section
        exclude = ['article', ]


class SubsectionForm(ElementForm, forms.ModelForm):

    class Meta:
        model = models.Subsection
        exclude = ['article', ]


class TextForm(ElementForm, forms.ModelForm):

    class Meta:
        model = models.Text
        exclude = ['article', ]


class TextForm(ElementForm, forms.ModelForm):

    class Meta:
        model = models.Text
        exclude = ['article', ]


class ImageForm(ElementForm, forms.ModelForm):

    class Meta:
        model = models.Image
        exclude = ['article', ]
        widgets = {'mediafile': forms.HiddenInput, }


class LinkForm(ElementForm, forms.ModelForm):
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


class QuoteForm(ElementForm, forms.ModelForm):

    class Meta:
        model = models.Quote
        exclude = ['article', ]


class LocationForm(ElementForm, forms.ModelForm):

    class Meta:
        model = models.Location
        exclude = ['article', ]


class SlideForm(ElementForm, forms.ModelForm):
    mediafiles = forms.CharField(
        required=False,
        max_length=1024, widget=forms.HiddenInput)

    class Meta:
        model = models.Slide
        exclude = ['article', 'album']

    def clean_mediafiles(self):
        res = self.cleaned_data.get('mediafiles', None) or '[]'
        if not hasattr(self.instance, 'album'):     # or self.instance.album.files.count() < 2:
            if res == '[]':
                raise forms.ValidationError(_('MediaFile is required'))
        return res

    @property
    def mediafiles_list(self):
        import json
        return json.loads(self.cleaned_data.get('mediafiles'))

    def save(self, *args, **kwargs):
        if not self.instance.article:
            self.instance.article = self.initial.get('article', None)

        if not self.instance.album_id:
            self.instance.album = Album.objects.create(
                owner=self.instance.article.author,
                title="New Album", )

        instance = super(SlideForm, self).save(*args, **kwargs)
        mediafiles = self.mediafiles_list
        if instance.album and mediafiles:
            if self.clean_mediafiles():
                instance.album.update_files(mediafiles)

        return instance


class ElementInsertForm(forms.Form):
    article = forms.ModelChoiceField(
        queryset=models.Article.objects.all(), widget=forms.HiddenInput)
    contenttype = forms.ModelChoiceField(
        queryset=ContentType.objects.all(), widget=forms.HiddenInput)
    position = forms.IntegerField(widget=forms.HiddenInput)

    @property
    def element_form_class(self):
        return ElementForm.for_model(
            self.cleaned_data['contenttype'].model_class())
