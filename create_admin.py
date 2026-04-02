from django.contrib.auth.models import User
import os
import django

# 1. DEFINE AS CONFIGURAÇÕES PRIMEIRO
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django2.settings')

# 2. INICIALIZA O DJANGO
django.setup()

# 3. SÓ DEPOIS DISSO IMPORTA O MODELO (Dentro da lógica)


def create_user():
    username = 'Pedro'
    email = 'plbrandsilva@email.com'
    password = 'Pl@23107'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Usuario {username} criado com sucesso!")
    else:
        print(f"Usuario {username} ja existe.")


if __name__ == "__main__":
    create_user()
