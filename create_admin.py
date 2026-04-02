from django.contrib.auth.models import User
import os
import django

# 1. Configura o módulo de settings PRIMEIRO
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django2.settings')

# 2. Inicializa o Django
django.setup()

# 3. SÓ AGORA importa os modelos

username = 'Pedro'
email = 'plbrandsilva@email.com'
password = 'Pl@23107'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Usuario {username} criado com sucesso!")
else:
    print(f"Usuario {username} ja existe.")
