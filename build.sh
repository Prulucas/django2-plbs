#!/usr/bin/env bash
# Interrompe a execução se houver erro em qualquer comando
set -o errexit

# 1. Instala as dependências (Django, gunicorn, dj-static, etc)
pip install -r requirements.txt

# 2. Reúne o CSS/JS na pasta 'staticfiles' para o dj-static ler
python manage.py collectstatic --no-input

# 3. Cria as tabelas no banco de dados PostgreSQL do Render
python manage.py migrate