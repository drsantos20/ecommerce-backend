from django.db import models


class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.PositiveIntegerField(help_text='in cents', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
