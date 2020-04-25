from django.db import models

from ecommerce.user.models.user_profile import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
