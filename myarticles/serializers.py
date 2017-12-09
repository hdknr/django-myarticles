from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property
from rest_framework import serializers
from mymedia.serializers import (
    OpenMediaFileSerializer, AlbumSerializer, MediaFileSerializer, )
from mylinks.serializers import PageSerializer
from mymedia.models import MediaFile, Album
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
    mediafile = MediaFileSerializer(many=False, read_only=True)

    class Meta:
        model = models.Image
        fields = '__all__'

    def to_representation(self, obj):
        data = super(ImageSerializer, self).to_representation(obj)
        data['mediafile_data'] = OpenMediaFileSerializer(obj.mediafile).data
        return data

    def to_internal_value(self, data):
        instance = super(ImageSerializer, self).to_internal_value(data)
        self._new_mediafile = instance
        mediafile_id = data.get('mediafile', {}).get('id', None)
        self.new_mediafile = mediafile_id and MediaFile.objects.filter(
            id=mediafile_id).first()
        return instance

    def update(self, instance, validated_data):
        if self.new_mediafile:
            instance.mediafile = self.new_mediafile
        return super(ImageSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        if self.new_mediafile:
            validated_data['mediafile'] = self.new_mediafile
        instance = super(ImageSerializer, self).create(validated_data)
        return instance


class LinkSerializer(AbstractElementSerializer):
    page = PageSerializer(many=False, read_only=True)

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
        print(self.updated_url, data)
        return instance

    @cached_property
    def new_page(self):
        if self.updated_url:
            ser = PageSerializer(data={'url': self.updated_url})
            if ser.is_valid():
                return ser.save()

    def update(self, instance, validated_data):
        if self.updated_url != instance.page.url:
            instance.page = self.new_page
        instance = super(LinkSerializer,
                         self).update(instance, validated_data)
        return instance

    def create(self, validated_data):
        if self.new_page:
            validated_data['page'] = self.new_page
        return super(LinkSerializer, self).create(validated_data)


class QuoteSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Quote
        fields = '__all__'


class LocationSerializer(AbstractElementSerializer):

    class Meta:
        model = models.Location
        fields = '__all__'


class SlideSerializer(AbstractElementSerializer):
    album = AlbumSerializer(many=False)

    class Meta:
        model = models.Slide
        fields = '__all__'

    def update(self, instance, validated_data):
        album_data = validated_data.pop('album', {})
        mediafiles = [i['id'] for i in album_data.get('mediafiles', [])]
        instance = super(SlideSerializer,
                         self).update(instance, validated_data)
        instance.album.update_files(mediafiles)
        return instance


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
