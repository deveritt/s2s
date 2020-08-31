from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .serializers import ProductSerialier
from .models import Product
import timeit
from django.db import connection
import json


class ProductViewSet(viewsets.ModelViewSet): #, ListCreateAPIView):
    """
    This is a generic API View.
    We can add custom filters as well as method routers later for things such as patch and permissions (on, say, delete).
    Also going url/pk/ will perform that http method on that particular record.
    Probably also want to add a Django user group with permissions to post.
    """
    serializer_class = ProductSerialier
    permission_classes = (permissions.AllowAny,)  # Should become permissions.IsAuthenticated
    model = Product
    queryset = Product.objects.all()
    # The below requires setting up of DRF filter_backends
    # filterset_fields = ("name", "sku",)
    # paginate_by = 10

    def create(self, request, *args, **kwargs):
        start = timeit.default_timer()
        result = []
        headers = {}

        # for data in request.data:
        #     pass
            # try:
            #
            #     new_product = Product(**data)
            #     new_product.clean()
            #     new_product.save()
            #     result.append("Added product SKU: {}.".format(data.get("sku", "Unknown")))
            #
            # except Exception as e:
            #
            #     result.append(
            #         "Skipping product SKU: {}; because of error: {}".format(data.get("sku", "Unknown"), e)
            #     )

        data = []
        for prod in request.data:
            record = (
                prod['sku'],
                prod['name'],
                str(prod['attributes']),
            )
            data.append(record)

        mySql_insert_query = """
          INSERT INTO products_product (sku, name, attributes)
          VALUES (%s, %s, %s)
        """

        with connection.cursor() as cursor:
            cursor.executemany(mySql_insert_query, data)

        serializer = self.serializer_class
        headers = self.get_success_headers(serializer.data)
        stop = timeit.default_timer()
        result.append("time: {}".format(stop - start))
        response = Response(result, status=status.HTTP_201_CREATED, headers=headers)
        return response
