from django.contrib import admin

# Register your models here.
from .models.customer import Customer
from .models import UserProfile


admin.site.register(UserProfile)
admin.site.register(Customer)
