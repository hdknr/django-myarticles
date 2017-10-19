# coding: utf-8
from django.db.models.signals import post_save
from django.dispatch import receiver
from mywords.models import Link
from . import models


@receiver(post_save, sender=models.Article)
def on_article_saved(sender, instance=None, **kwargs):
    if instance and instance.keywords:
        instance.update_links()
