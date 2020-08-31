from rest_framework import serializers
from .models import Product


class ProductSerialier(serializers.ModelSerializer):
    """
    This takes care of serializing the model and running any validatiuon rules necessary.
    """
    class Meta:

        model = Product
        fields = [
            'sku',
            'name',
            'attributes'
        ]
        # lookup_field = "name"
