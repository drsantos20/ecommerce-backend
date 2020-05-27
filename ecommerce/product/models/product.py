from django.db import models
from rest_framework import serializers


class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.PositiveIntegerField(help_text='in cents', blank=True, null=True)

    @classmethod
    def get_serializer(cls):
        class BaseSerializer(serializers.ModelSerializer):
            class Meta:
                model = cls
                fields = '__all__'

        return BaseSerializer
