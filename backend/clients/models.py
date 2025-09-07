from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=111)
    full_address = models.CharField(max_length=111)