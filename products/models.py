from django.db import models
import jsonfield


class Product(models.Model):
    sku = models.CharField(max_length=255, db_index=True, unique=True)  # Indexed for API access.
    name = models.CharField(max_length=255, db_index=True)  # Indexed for later searching.
    attributes = jsonfield.JSONField()

    class Meta:
        def __unicode__(self):
            return "{} ({})".format(self.sku, self.name)

