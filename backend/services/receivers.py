from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_delete

from services.models import Subscription

@receiver(post_delete, sender=None)
def delete_cache_total_sum(*args, **kwargs):
    cache.delete('price_cache')