import os
import django
import logging
from datetime import datetime

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from app.models import KeyValueJsonStoreTTL
from django.utils import timezone

def delete_expired_values():
    KeyValueJsonStoreTTL.objects.filter(expires_at__lt=timezone.now()).delete()
    # Log the action with the current time
    logging.info("Ran background check and deleted expired values.")

if __name__ == "__main__":
    delete_expired_values()
