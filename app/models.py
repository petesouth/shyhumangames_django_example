from django.db import models
from django.utils import timezone
from datetime import timedelta

class KeyValueJsonStoreTTL(models.Model):
    key = models.CharField(max_length=255, unique=True, db_index=True)
    value = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=5)  # Set TTL as 5 minutes
        super().save(*args, **kwargs)



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
