#!/usr/bin/env bash
# Interrompe se houver erro
set -o errexit

# 1. Dependências
pip install -r requirements.txt

# 2. Estáticos e Migrações
python manage.py collectstatic --no-input
python manage.py migrate

# 3. CRIAÇÃO DO SUPERUSUÁRIO (Versão Robusta)
# Esta linha configura o ambiente e cria o user em um único comando seguro
export DJANGO_SETTINGS_MODULE=django2.settings

python -c "
import django
django.setup()
from django.contrib.auth.models import User
username = 'Pedro'
email = 'plbrandsilva@email.com'
password = 'Pl@23107'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Usuario Pedro criado com sucesso!')
else:
    print('Usuario Pedro ja existe.')
"