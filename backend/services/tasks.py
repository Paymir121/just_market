import time
from datetime import datetime

from celery import shared_task
from django.core.cache import cache
from django.db import transaction
from django.db.models import F
from celery_singleton import Singleton


@shared_task(base=Singleton)
def set_price(subscription_id):
    with transaction.atomic():
        from services.models import Subscription
        subscription = Subscription.objects.select_for_update().filter(id=subscription_id).annotate(
            annotate_price=F("service__full_price")*(1-F("plan__discount_percent")/100.00)
        ).first()
        subscription.price = subscription.annotate_price
        subscription.save()
    cache.delete('price_cache')


@shared_task(base=Singleton)
def set_comment(subscription_id):
    with transaction.atomic():
        from services.models import Subscription
        subscription = Subscription.objects.select_for_update().get(id=subscription_id)
        subscription.comment = str(datetime.now())
        subscription.save()
    cache.delete('price_cache')

