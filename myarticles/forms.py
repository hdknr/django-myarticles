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
        exclude = []


class SubsectionForm(forms.ModelForm):

    class Meta:
        model = models.Subsection
        exclude = []


class TextForm(forms.ModelForm):

    class Meta:
        model = models.Text
        exclude = []


class TextForm(forms.ModelForm):

    class Meta:
        model = models.Text
        exclude = []


class ImageForm(forms.ModelForm):

    class Meta:
        model = models.Image
        exclude = []


class LinkForm(forms.ModelForm):

    class Meta:
        model = models.Link
        exclude = []


class QuoteForm(forms.ModelForm):

    class Meta:
        model = models.Quote
        exclude = []


class LocationForm(forms.ModelForm):

    class Meta:
        model = models.Location
        exclude = []
