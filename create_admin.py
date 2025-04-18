# create_admin.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grandmas_kitchen.settings")  # change 'your_project_name'
django.setup()

from django.contrib.auth.models import User

username = "Vamshi@admin"
password = "rishi123@"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email="", password=password)
    print("Superuser created.")
else:
    print("Superuser already exists.")
