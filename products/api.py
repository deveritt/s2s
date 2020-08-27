from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .serializers import ProductSerialier
from .models import Product


class ProductViewSet(ListCreateAPIView):
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

    def create(self, request, *args, **kwargs):

        for data in request.data:

            new_product = Product(**data)
            new_product.clean()
            new_product.save()

            serializer = self.serializer_class
            headers = self.get_success_headers(serializer.data)

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

