import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from app.models import KeyValueJsonStoreTTL
from django.utils import timezone

def delete_expired_values():
    KeyValueJsonStoreTTL.objects.filter(expires_at__lt=timezone.now()).delete()

if __name__ == "__main__":
    delete_expired_values()
