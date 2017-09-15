# coding: utf-8

from myarticles import forms

FORMS = {
    'link': forms.LinkForm,
    'image': forms.ImageForm,
    'location': forms.LocationForm,
    'quote': forms.QuoteForm,
    'section': forms.SectionForm,
    'subsection': forms.SubsectionForm,
    'text': forms.TextForm,
}


def form_for_contenttype(content_type):
    return  FORMS[content_type.model]


def form_for_symbol(name):
    return  FORMS[name]
