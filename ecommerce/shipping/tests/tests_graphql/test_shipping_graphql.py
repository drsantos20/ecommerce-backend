import json

from graphene_django.utils import GraphQLTestCase

from ecommerce.user.schema import Query
from ecommerce.shipping.factories import SeaFactory


class SeaShippingTestQuery(GraphQLTestCase):
    GRAPHQL_SCHEMA = Query
    GRAPHQL_URL = '/ecommerce/v1/shipping/'

    def setUp(self):
        self.sea = SeaFactory()

    def test_get_shipping_by_order_id(self):
        response = self.query(
            '''
            query shipping($id: Int!){
                shipping(id: $id) {
                    order
                }
            }
            ''',
            variables={'id': 1}
        )

        content = json.loads(response.content)
        import pdb; pdb.set_trace()
        print(response.content)
        self.assertEqual(response.status_code, 200)


        shipping_from_query = content['data']['shipping']

        self.assertEqual(shipping_from_query['order'], self.sea.order.id)
