from http.client import responses
from django.core.cache import cache
from django.db.models import Prefetch, F, Sum
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import Subscription

from services.serializers import SubscriptionSerializer

from clients.models import Client


# Create your views here.
class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        Prefetch("client", queryset=Client.objects.all().select_related("user").only("company_name", "user__email"))
    )
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        price_cache = cache.get('price_cache')
        if price_cache:
            total_price = price_cache
        else:
            total_price = queryset.aggregate(total=Sum("price")).get("total")
            cache.set('price_cache', total_price, 60*60)
        response_data = {
            "result": response.data,
            "total_amount": total_price
        }
        response.data =  response_data
        return response
