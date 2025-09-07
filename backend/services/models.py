from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=111)
    full_price = models.PositiveIntegerField

class Plan(models.Model):
    PLAN_TYPES = (
        ("full", "Full",),
        ("student", "Student",),
        ("discount", "Discount",)
    )
    plant = models.CharField(choices=PLAN_TYPES, max_length=111)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ]
                                                   )
class Subscription(models.Model):
    client = models.ForeignKey("clients.Client", related_name="subscriptions", on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name="subscriptions", on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name="subscriptions", on_delete=models.PROTECT)