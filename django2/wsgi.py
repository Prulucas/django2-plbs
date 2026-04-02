import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling  # Certifique-se que instalou dj-static

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django2.settings')

# Esta linha deve estar EXATAMENTE assim:
application = Cling(MediaCling(get_wsgi_application()))
