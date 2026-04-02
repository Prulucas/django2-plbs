# create_admin.py
from django.contrib.auth.models import User
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django2.settings')
django.setup()


username = 'Pedro'
email = 'plbrandsilva@email.com'
password = 'Pl@23107'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Usuario {username} criado com sucesso!")
else:
    print(f"Usuario {username} ja existe.")
