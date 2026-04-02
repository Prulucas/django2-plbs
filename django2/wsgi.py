import os
from django.core.wsgi import get_wsgi_application
# Importa as ferramentas de arquivos estáticos e mídia
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django2.settings')

# O Cling cuida do STATIC e o MediaCling cuida do MEDIA (fotos dos consoles)
application = Cling(MediaCling(get_wsgi_application()))
