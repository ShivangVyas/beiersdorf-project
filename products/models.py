from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    price_description = models.CharField(max_length=255, blank=True)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)   # 2083 is the max length for urls
    # content:
    carbohydrate = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
