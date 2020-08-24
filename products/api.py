from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerialier
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerialier
    permission_classes = (permissions.AllowAny,)  # Should become permissions.IsAuthenticated
    queryset = Product.objects.all()
