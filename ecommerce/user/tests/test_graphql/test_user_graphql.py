import json

from graphene_django.utils.testing import GraphQLTestCase

from ecommerce.schema import Query, Mutation, schema
from ecommerce.user.factories import UserProfileFactory


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

    def test_get_user_by_id(self):
        response = self.query(
            '''
            query user($id: Int!){
                user(id: $id) {
                    email,
                    location
                }
            }
            ''',
            variables={'id': 1}
        )

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        user_from_query = content['data']['user']

        self.assertEqual(user_from_query['email'], self.user.email)
        self.assertEqual(user_from_query['location'], self.user.location)


class UserProfileMutation(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = '/ecommerce/v1/users/'

    def setUp(self):
        self.user = UserProfileFactory(email='solid_snake@gmail.com')

    def test_update_user(self):
        response = self.query(
            '''
            mutation updateUser($email: String!, $location: String!){
                updateUser(email: $email, location: $location) {
                    user {
                        email,
                        location
                    }
                }
            }
            ''',
            variables={'email': self.user.email, 'location': 'London'}
        )

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        user_from_query = content['data']['updateUser']['user']

        self.assertEqual(user_from_query['email'], self.user.email)
        self.assertEqual(user_from_query['location'], 'London')

    def test_crete_user(self):
        response = self.query(
            '''
            mutation createUser($email: String!, $username: String!){
                createUser(email: $email, username: $username) {
                    user {
                        email
                    }
                }
            }
            ''',
            variables={'email': 'batman@dc.com', 'username': 'batman'}
        )

        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        user_from_query = content['data']['createUser']['user']

        self.assertEqual(user_from_query['email'], 'batman@dc.com')
