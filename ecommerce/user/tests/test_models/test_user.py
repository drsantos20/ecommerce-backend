from datetime import datetime

from django.test import TestCase

from ecommerce.user.factories import UserProfileFactory
from ecommerce.user.models.user_profile import UserProfile


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserProfileFactory(email='snake@mtgs.com')

    def test_get_user(self):
        user = UserProfile.objects.get(email='snake@mtgs.com')

        self.assertEqual(self.user.email, user.email)
        self.assertEqual(self.user.user_type, user.user_type)
        self.assertEqual(self.user.location, user.location)
