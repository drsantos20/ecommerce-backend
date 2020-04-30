from django.test import TestCase

from ecommerce.user.factories import UserProfileFactory
from ecommerce.user.serializers.user_serializer import UserProfileSerializer


class TestUserProfileSerializer(TestCase):
    def setUp(self) -> None:
        self.user = UserProfileFactory()
        self.user_profile_serializer = UserProfileSerializer(self.user)

    def test_get_user_serializer(self):
        serializer_data = self.user_profile_serializer.data
        self.assertEqual(serializer_data['email'], self.user.email)
        self.assertEqual(serializer_data['location'], self.user.location)
        self.assertEqual(serializer_data['user_type'], self.user.user_type)
