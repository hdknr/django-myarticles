# coding: utf-8
from django.utils.safestring import SafeString as _S
from django.utils.translation import ugettext_lazy as _
from django.template import Template, Context
from corekit import admin as core_admin
from ordered_model.admin import OrderedTabularInline
from . import models, forms


def admin_change_link(obj):
    url = 'admin:{}_{}_change'.format(
        obj._meta.app_label, obj._meta.model_name)
    t = Template('''<a href="{% url u i.id %}">{{ i }}</a>''')
    res = t.render(Context({'u': url,  'i': obj}))
    return res


class ElementAdminInline(OrderedTabularInline):
    model = models.Element
    extra = 0
    readonly_fields = ['id', 'content_type', 'instance_admin', 'order', 'move_up_down_links', ]

    def instance_admin(self, obj):
        return admin_change_link(obj.instance)


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
    readonly_fields = ['page_link']
    raw_id_fields = ElementAdmin.raw_id_fields + ['page']
    form = forms.LinkForm

    def page_link(self, obj):
        return admin_change_link(obj.page)

    page_link.short_description = _('Web Page')


class QuoteAdmin(ElementAdmin):
    pass


class ImageAdmin(ElementAdmin):
    pass


class LocationAdmin(ElementAdmin):
    pass


class SlideAdmin(ElementAdmin):
    raw_id_fields = ElementAdmin.raw_id_fields + ['album']


core_admin.register(__name__, globals(), [],)
