#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Chama o script Python de forma limpa, sem aspas confusas no shell
python create_admin.py