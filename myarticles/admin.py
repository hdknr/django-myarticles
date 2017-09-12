# coding: utf-8
from corekit import admin as core_admin


class ArticleAdmin(core_admin.CoreAdmin):
    raw_id_fields = ['author']


class ElementAdmin(core_admin.CoreAdmin):
    raw_id_fields = ['article']


class SectionAdmin(ElementAdmin):
    pass


class SubsectionAdmin(ElementAdmin):
    pass


class TextAdmin(ElementAdmin):
    pass


class LinkAdmin(ElementAdmin):
    pass


class QuoteAdmin(ElementAdmin):
    pass


class ImageAdmin(ElementAdmin):
    pass


class LocationAdmin(ElementAdmin):
    pass


core_admin.register(__name__, globals(), [],)
