from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from mymedia.serializers import (
    OpenMediaFileSerializer, AlbumSerializer, MediaFileSerializer, )
from mylinks.serializers import PageSerializer
from . import models, conf


class ArticleSerializer(serializers.ModelSerializer):
    catch = MediaFileSerializer(many=False, read_only=True)

    class Meta:
        model = models.Article
        fields = '__all__'


class ContentTypeField(serializers.Field):
    SPLITER = '_'

    def to_representation(self, obj):
        return self.SPLITER.join(obj.natural_key())

    def to_internal_value(self, data):
        return ContentType.objects.get_by_natural_key(*data.split(self.SPLITER))


class AbstractElementSerializer(serializers.ModelSerializer):
    content_type = ContentTypeField()

    def post_save(self, instance):
        request = self.context.get('request', None)
        if 'order' in request.data:
            instance.to(int(request.data['order']))       # MOVE
        return instance

    def update(self, instance, validated_data):
        instance = super(AbstractElementSerializer,
                         self).update(instance, validated_data)
        return self.post_save(instance)

    def create(self, validated_data):
        instance = super(AbstractElementSerializer, self).create(validated_data)
        return self.post_save(instance)


class SectionSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Section
        fields = '__all__'


class SubsectionSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Subsection
        fields = '__all__'


class TextSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Text
        fields = '__all__'


class ImageSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'

    def to_representation(self, obj):
        data = super(ImageSerializer, self).to_representation(obj)
        data['mediafile_data'] = OpenMediaFileSerializer(obj.mediafile).data
        return data


class LinkSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Link
        fields = '__all__'

    def to_representation(self, obj):
        data = super(LinkSerializer, self).to_representation(obj)
        data['page_data'] = PageSerializer(obj.page).data
        return data

    def to_internal_value(self, data):
        instance = super(LinkSerializer, self).to_internal_value(data)
        self.updated_url = data.get('page_data', {}).get('url', None)
        return instance

    def update(self, instance, validated_data):
        instance = super(LinkSerializer,
                         self).update(instance, validated_data)
        if self.updated_url and instance.page.url != self.updated_url:
            self.instance.page.url = self.updated_url
            self.instance.page.save()
        return instance

class QuoteSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Quote
        fields = '__all__'


class LocationSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Location
        fields = '__all__'


class SlideSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Slide
        fields = '__all__'

    def to_representation(self, obj):
        data = super(SlideSerializer, self).to_representation(obj)
        data['alubm_data'] = AlbumSerializer(obj.album).data
        return data


class ElementSerializer(serializers.ModelSerializer):

    content_type = ContentTypeField()

    class Meta:
        model = models.Element
        fields = '__all__'

    @classmethod
    def get_concrete_serializer(cls, klass):
        for ser in AbstractElementSerializer.__subclasses__():
            if klass == ser.Meta.model:
                return ser

    def to_representation(self, obj):
        ser = self.get_concrete_serializer(obj.instance._meta.model)
        return ser and ser(obj.instance).data \
            or super(ElementSerializer, self).to_representation(obj)
