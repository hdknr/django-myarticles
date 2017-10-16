# coding: utf-8
from django.utils.safestring import SafeString as _S
from corekit import admin as core_admin
from ordered_model.admin import OrderedTabularInline
from . import models


class ElementAdminInline(OrderedTabularInline):
    model = models.Element
    extra = 0
    readonly_fields = ['id', 'instance_admin', 'order', 'move_up_down_links', ]

    def instance_admin(self, obj):
        return _S('<a href="{}">{}</a>'.format(
            obj.instance.admin_change_url(),
            obj.instance))


class ArticleAdmin(core_admin.CoreAdmin):
    raw_id_fields = ['author', 'catch']
    inlines = [ElementAdminInline, ]

    def get_urls(self):
        urls = super(ArticleAdmin, self).get_urls()
        for inline in self.inlines:
            if hasattr(inline, 'get_urls'):
                urls = inline.get_urls(self) + urls
        return urls


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
