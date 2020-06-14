from django.db import models

from ecommerce.user.models import UserProfile


class Customer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
