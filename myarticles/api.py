from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'article', viewsets.ArticleViewSet, base_name='article')
router.register(r'element', viewsets.ElementViewSet, base_name='element')

urlpatterns = [
    url(r'^', include(router.urls)),
]
