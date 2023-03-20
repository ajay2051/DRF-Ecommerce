from settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'drfecommerce',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost'
    }
}
