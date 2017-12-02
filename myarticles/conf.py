from myarticles import forms, serializers

FORMS = {
    'section': forms.SectionForm,
    'subsection': forms.SubsectionForm,
    'link': forms.LinkForm,
    'image': forms.ImageForm,
    'location': forms.LocationForm,
    'quote': forms.QuoteForm,
    'text': forms.TextForm,
    'slide': forms.SlideForm,
}

def form_for_contenttype(content_type):
    return  FORMS[content_type.model]


def form_for_symbol(name):
    return  FORMS[name]
