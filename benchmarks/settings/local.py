# -*- coding:utf-8 -*-

from .base import *

DEBUG = True

DATABASES = {
    'default': {},
    'mysql': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bm',
        'USER': 'root',
        'PASSWORD': 'jj891030',
        'HOST': '119.29.171.154',
        'PORT': '3306',
    },
    'psql': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bm',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '119.29.171.154',
        'PORT': '5432',
    },
    'mongo': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'djongo',
        'NAME': 'bm',
        # 'NAME': 'bm',
        'HOST': '119.29.171.154',
        'PORT': 27017,
    }
}

GET_MATCHED_STATION_LIST_URL = \
    'http://127.0.0.1:8002/accounting/express/v1.2/warehouses/match_station_list'
GET_STATION_INFO_URL = \
    'http://127.0.0.1:8002/accounting/express/v1.2/stations/'

REDIS_CONFIG = {
    'orderjob': {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 6379,
        'REDIS_DB': '0',
        'REDIS_PASSWORD': ''
    },
    'raw_order': {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 6379,
        'REDIS_DB': '1',
        'REDIS_PASSWORD': ''
    },
    'log_server': {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 6379,
        'REDIS_DB': '2',
        'REDIS_PASSWORD': ''
    },
    'default': {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 6379,
        'REDIS_DB': '3',
        'REDIS_PASSWORD': ""
    },
    'user': {
        'REDIS_HOST': 'test.xbmhz.com',
        'REDIS_PORT': 7218,
        'REDIS_DB': '4',
        'REDIS_PASSWORD': 'YcMi@7@lVroX@d6ewmE+@83o3Cj#rf'
    },
}
MQ_CONFIG = {
    'log_server': {
        'HOST': "127.0.0.1",
        'PORT': 5672,
        'USERNAME': 'guest',
        'PASSWORD': "guest"
    },
    'default': {
        'SERVER': '127.0.0.1',
        'PORT': 5672,
        'VHOST': '/',
        'USER': 'guest',
        'PASSWORD': 'guest',
    }
}
