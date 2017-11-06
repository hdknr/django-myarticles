from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.Article)
def on_article_saved(sender, instance=None, **kwargs):
    if instance.element_set.count() ==0:
        models.Section.objects.create(article=instance)
