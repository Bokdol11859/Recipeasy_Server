from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ['recipeasy.link', '127.0.0.1', '3.35.14.95', '172.31.10.111']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}
