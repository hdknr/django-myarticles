# coding: utf-8
from django import forms
from . import models


class ArticleForm(forms.ModelForm):

    class Meta:
        model = models.Article
        exclude = []


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

    class Meta:
        model = models.Link
        exclude = ['article', ]


class QuoteForm(forms.ModelForm):

    class Meta:
        model = models.Quote
        exclude = ['article', ]


class LocationForm(forms.ModelForm):

    class Meta:
        model = models.Location
        exclude = ['article', ]
