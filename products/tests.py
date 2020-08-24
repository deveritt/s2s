from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product


class ProductApiTests(APITestCase):

    url = reverse('products-list')

    def test_create_list_product(self):
        """
        Ensure we can create a new product.
        """
        data = {
            "sku": "abc",
            "name": "testprod",
            "attributes": {
                "size": "small",
                "grams": "100",
                "foo": "bar"
            }
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'testprod')
