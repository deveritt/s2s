from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerialier
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    This is a generic API View.
    We can add custom filters as well as method routers later for things such as patch and permissions (on, say, delete).
    Also going url/pk/ will perform that http method on that particular record.
    Probably also want to add a Django user group with permissions to post.
    """
    serializer_class = ProductSerialier
    permission_classes = (permissions.AllowAny,)  # Should become permissions.IsAuthenticated
    queryset = Product.objects.all()
    # The below requires setting up of DRF filter_backends
    # filterset_fields = ("name", "sku",)
