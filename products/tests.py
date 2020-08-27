from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product


class ProductApiTests(APITestCase):

    # url = reverse('products')
    url = reverse('products-list')

    def test_create_list_product(self):
        """
        Ensure we can create a new product.
        """
        data = [{
            "sku": "abc",
            "name": "testprod",
            "attributes": {
                "size": "small",
                "grams": "100",
                "foo": "bar"
            }
        },
        ]
        for aprod in range(100):
            data.append({
                "sku": "abc{}".format(aprod),
                "name": "testprod{}".format(aprod),
                "attributes": {
                    "some": "arb",
                    "attib": "utes"
                }
            })
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 101)
        self.assertEqual(Product.objects.first().name, 'testprod')
