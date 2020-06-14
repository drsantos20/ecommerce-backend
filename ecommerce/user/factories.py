import datetime

import factory
from django.contrib.auth.models import User

from ecommerce.user.models import Customer
from ecommerce.user.models.user_profile import UserProfile


class UserFactory(factory.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')

    class Meta:
        model = User


class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user_type = factory.Iterator([1, 2])
    location = factory.Iterator(["France", "Italy", "Spain"])
    birth_date = factory.LazyFunction(datetime.date.today)
    email = factory.Iterator(["drsantos20@gmail.com", "batman@dc.com", "flash@dc.com"])
    user = factory.SubFactory(UserFactory)


class CustomerFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    order = factory.SubFactory('ecommerce.order.factories.OrderFactory')

    class Meta:
        model = Customer
