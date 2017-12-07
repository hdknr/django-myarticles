from django.contrib.contenttypes.models import ContentType
from collections import OrderedDict
from rest_framework import viewsets, pagination, permissions
from rest_framework.response import Response
from mymedia.models import MediaFile
from . import models, serializers, filters


class Pagination(pagination.PageNumberPagination):
    page_size = 16
    max_page_size = 16
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_range', list(self.page.paginator.page_range)),
            ('current_page', self.page.number),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    filter_class = filters.ArticleFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = Pagination

    def perform_update(self, serializer):
        catch = MediaFile.objects.filter(
            id=self.request.data.get('catch', {}).get('id', None)).first()
        params = catch and {'catch': catch} or {}
        serializer.save(**params)


class ElementViewSet(viewsets.ModelViewSet):

    queryset = models.Element.objects.all()
    serializer_class = serializers.ElementSerializer
    filter_class = filters.ElementFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_object(self):
        instance = super(ElementViewSet, self).get_object()
        return instance.instance

    def get_content_type(self):
        ''' Find Element subclass serializer based
            on 'id' or 'content_type' in `data`  '''
        id = self.request.data.get('id', None)
        if id:
            return ContentType.objects.filter(element__id=id).first()

        content_type = self.request.data.get('content_type', None)
        if content_type:
            return ContentType.objects.get_by_natural_key(
                *content_type.split('.'))


    def get_serializer_class(self):
        ''' dynamically change serializer '''
        if self.request.method == 'GET' or not self.request.data:
            return super(ElementViewSet, self).get_serializer_class()

        content_type = self.get_content_type()
        if content_type:
            return serializers.ElementSerializer.get_concrete_serializer(
                content_type.model_class())
        return super(ElementViewSet, self).get_serializer_class()
