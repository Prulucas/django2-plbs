#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Adicione esta linha (ajuste o nome, email e senha)
# Ela verifica se o usuário já existe antes de tentar criar
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('Pedro', 'plbrandsilva@email.com', 'Pl@23107')"