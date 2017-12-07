# coding: utf-8
from django.contrib.contenttypes.models import ContentType
from corekit import views as core_views
from . import filters, models, forms, conf


class ArticleView(core_views.View):

    @core_views.handler(
        url=r'(?P<id>\d+)',
        name="myarticles_article_detail", order=70,
        perms=['articles.change_article'])
    def detail(self, request, id):
        instance = models.Article.objects.filter(id=id).first()

        if not instance.check_perm(request.user):
            return self.not_authorized()

        return self.render(
            'articles/article/detail.html', instance=instance)
            
    @core_views.handler(
        url=r'(?P<id>\d+)/meta/edit',
        name="myarticles_article_meta_edit", order=60,
        perms=['articles.change_article'])
    def meta_edit(self, request, id):
        instance = models.Article.objects.filter(id=id).first()

        if not instance.check_perm(request.user):
            return self.not_authorized()

        form = forms.ArticleForm(request.POST or None, instance=instance)
        mode = request.POST.get('mode', None) or 'edit'
        if mode == 'edit' and request.method == 'POST' and form.is_valid():
            form.save()
            mode = 'detail'

        return self.render(
            'articles/article/meta/{}.html'.format(mode),
            instance=instance, form=form)

    @core_views.handler(
        url=r'(?P<id>\d+)/meta$',
        name="myarticles_article_meta_detail", order=60,
        perms=['articles.change_article'])
    def meta_detail(self, request, id):
        instance = models.Article.objects.filter(id=id).first()
        return self.render(
            'articles/article/meta/detail.html', instance=instance)


class ElementView(core_views.View):

    def template_name(self, instance_or_contenttype, name):
        contentype =  instance_or_contenttype \
            if isinstance(instance_or_contenttype, ContentType) \
                else instance_or_contenttype.contenttype()

        res = 'articles/element/{1}.{2}/{0}.html'.format(
            name, *contentype.natural_key())
        return res

    @core_views.handler(
        url=r'element/(?P<id>\d+)$',
        name="myarticles_element_detail", order=70,
        perms=['articles.change_element'])
    def detail(self, request, id):
        instance = models.Element.objects.filter(id=id).first()
        instance = instance and instance.instance
        if not instance:
            return self.page_not_found()

        return self.render(
            self.template_name(instance, 'detail'), instance=instance)

    @core_views.handler(
        url=r'element/(?P<id>\d+)/edit',
        name="myarticles_element_edit", order=60,
        perms=['articles.change_article'])
    def edit(self, request, id):
        instance = models.Element.objects.filter(id=id).first()
        if not instance.article.check_perm(request.user):
            return self.not_authorized()

        instance = instance and instance.instance
        form_class = conf.form_for_contenttype(instance.contenttype())
        form = form_class(request.POST or None, instance=instance)

        mode = request.POST.get('mode', None) or 'edit'
        if mode == 'edit' and request.method == 'POST' and form.is_valid():
            form.save()
            mode = 'detail'
        elif mode == 'delete':
            instance.delete()

        return self.render(
            self.template_name(instance, mode), form=form, instance=instance)

    @core_views.handler(
        url=r'element/move',
        name="myarticles_element_move", order=60,
        perms=['articles.change_article'])
    def move(self, request):
        to = request.POST.get('to', '')
        id = request.POST.get('id', '')
        instance = models.Element.objects.filter(id=id).first()

        if not instance:
            return self.page_not_found()
        if not instance.article.check_perm(request.user):
            return self.not_authorized()

        if to.isdigit():
            instance.to(int(to))
        instance = instance.instance
        return self.render(
            self.template_name(instance, 'detail'), instance=instance)

    @core_views.handler(
        url=r'element/insert',
        name="myarticles_element_insert", order=60,
        perms=['articles.change_article'])
    def insert(self, request):
        insert_form = forms.ElementInsertForm(
            request.POST or None, prefix="insert-element")

        if not insert_form.is_valid():
            return self.render('error')

        article = insert_form.cleaned_data.get('article', None)
        if not article or not article.check_perm(request.user):
            return self.not_authorized()

        form = insert_form.element_form_class(
            request.POST or None, initial={'article': article})

        mode = request.POST.get('mode', None) or 'insert'
        if mode == 'insert' and request.method == 'POST' and form.is_valid():
            form.instance.article = insert_form.cleaned_data['article']
            instance = form.save()
            instance.to(insert_form.cleaned_data['position'] + 1)   # 位置
            return self.render(
                self.template_name(instance, 'detail'), instance=instance)

        return self.render(
            self.template_name(
                insert_form.cleaned_data['contenttype'], mode),
            form=form, insert_form=insert_form)
