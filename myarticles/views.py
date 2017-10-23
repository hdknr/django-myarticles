# coding: utf-8
from corekit import views as core_views
from . import filters, models, forms, conf


class ArticleView(core_views.View):

    @core_views.handler(
        url=r'',
        name="myarticles_article_index", order=90,
        perms=['articles.change_article'])
    def index(self, request):
        instances = filters.ArticleFilter(request.GET)
        return self.render(
            'articles/article/index.html', instances=instances)

    @core_views.handler(
        url=r'(?P<id>\d+)',
        name="myarticles_article_detail", order=70,
        perms=['articles.change_article'])
    def detail(self, request, id):
        instance = models.Article.objects.filter(id=id).first()
        return self.render(
            'articles/article/detail.html', instance=instance)

    @core_views.handler(
        url=r'(?P<id>\d+)/meta/edit',
        name="myarticles_article_meta_edit", order=60,
        perms=['articles.change_article'])
    def meta_edit(self, request, id):
        instance = models.Article.objects.filter(id=id).first()
        form = forms.ArticleForm(request.POST or None, instance=instance)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return self.render(
                'articles/article/meta/detail.html',
                instance=instance, form=form)
        return self.render(
            'articles/article/meta/edit.html', instance=instance, form=form)

    @core_views.handler(
        url=r'(?P<id>\d+)/meta$',
        name="myarticles_article_meta_detail", order=60,
        perms=['articles.change_article'])
    def meta_detail(self, request, id):
        instance = models.Article.objects.filter(id=id).first()
        return self.render(
            'articles/article/meta/detail.html', instance=instance)

    @core_views.handler(
        url=r'(?P<id>\d+)/edit',
        name="myarticles_article_edit", order=70,
        perms=['articles.change_article'])
    def edit(self, request, id):
        instance = models.Article.filter(id=id).first()
        form = forms.ArtileForm(request.POST or None, instance=instance)
        if request.method == 'POST' and form.is_valid():
            form.save()
        return self.render(
            'articles/article/edit.html', form=form)


class ElementView(core_views.View):

    def template_name(self, instance, name):
        return 'articles/element/{1}.{2}/{0}.html'.format(
            name, *instance.contenttype().natural_key())

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
        instance = instance and instance.instance
        form_class = conf.form_for_contenttype(instance.contenttype())
        form = form_class(request.POST or None, instance=instance)

        mode = 'edit'
        if request.method == 'POST' and form.is_valid():
            form.save()
            mode = request.POST.get('mode', mode) or 'detail'
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
        position = request.POST.get('position', '')
        article_id = request.POST.get('article_id', '')
        app_label = request.POST.get('app_label', '')
        model_name = request.POST.get('model_name', '')

        instance = models.Element.objects.filter(id=id).first()
        if not instance:
            return self.page_not_found()
        if to.isdigit():
            instance.to(int(to))
        instance = instance.instance
        return self.render(
            self.template_name(instance, 'detail'), instance=instance)
