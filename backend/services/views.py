from django.db.models import Prefetch, F
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import Subscription

from services.serializers import SubscriptionSerializer

from clients.models import Client


# Create your views here.
class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        Prefetch("client", queryset=Client.objects.all().select_related("user").only("company_name", "user__email"))
    ).annotate(
        price=F("services__full_price") * (1 - F("services__discount_percent") / 100)
    )
    serializer_class = SubscriptionSerializer