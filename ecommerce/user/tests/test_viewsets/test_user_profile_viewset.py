import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from ecommerce.user.factories import UserProfileFactory


class TestUserProfileViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserProfileFactory()

    def test_get_all_users(self):
        response = self.client.get(
            reverse('user-list', kwargs={'version': 'v1', 'type': 'userprofile'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_data = json.loads(response.content)[0]

        self.assertEqual(user_data['email'], self.user.email)
        self.assertEqual(user_data['location'], self.user.location)
        self.assertEqual(user_data['user_type'], self.user.user_type)
