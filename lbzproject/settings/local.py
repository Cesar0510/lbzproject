#! /usr/bin/env python

from .base import *

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME':'lbzproject' ,
            'USER': 'lbzproject',
            'PASSWORD':'lbzproject',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
