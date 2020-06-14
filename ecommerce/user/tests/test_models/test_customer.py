from django.test import TestCase

from ecommerce.user.factories import CustomerFactory, UserProfileFactory
from ecommerce.user.models.customer import Customer


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserProfileFactory(email='snake@mtgs.com')
        self.customer = CustomerFactory(user=self.user)

    def test_get_user(self):
        customer = Customer.objects.get(id=self.customer.id)

        self.assertEqual(self.customer.user.email, customer.user.email)
        self.assertEqual(self.customer.user.user_type, customer.user.user_type)
        self.assertEqual(self.customer.user.location, customer.user.location)
