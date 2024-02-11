from django.db import models

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    license_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    logo = models.URLField()
    email = models.EmailField()
    rating_score = models.FloatField()
    rating_count = models.IntegerField()
    comments_count = models.IntegerField()
    popularity = models.IntegerField()
    city = models.IntegerField()

# Create your models here.
