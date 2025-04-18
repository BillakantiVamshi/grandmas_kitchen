import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grandmas_kitchen.settings")  # replace with your actual project name
django.setup()

from app1.models import Account  # This is your custom user model

username = "Vamshi@admin"
password = "rishi123@"

if not Account.objects.filter(username=username).exists():
    Account.objects.create_superuser(username=username, email="", password=password)
    print("Superuser created.")
else:
    print("Superuser already exists.")
    