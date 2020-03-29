import json

from graphene_django.utils.testing import GraphQLTestCase

from ecommerce.schema import schema, Query
from ecommerce.user.factories import UserFactory, UserProfileFactory


class UserProfileTestQuery(GraphQLTestCase):
    GRAPHQL_SCHEMA = Query
    GRAPHQL_URL = '/ecommerce/v1/users/'

    def setUp(self):
        self.user = UserProfileFactory(email='solid_snake@gmail.com')

    def test_user_query(self):
        response = self.query(
            '''
            query {
                allUsers {
                    email
                    birthDate
                    location
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        user_from_query = content['data']['allUsers'][0]

        self.assertEqual(user_from_query['email'], self.user.email)
        self.assertEqual(user_from_query['location'], self.user.location)

