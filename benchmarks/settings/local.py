# -*- coding:utf-8 -*-

from .base import *

DEBUG = True

# APP_CENTER = {
#     "ip": "127.0.0.1",
#     "port": 8003
# }
APP_CENTER_URL = '127.0.0.1:8003'
GET_USER_INFO_URL = 'http://127.0.0.1:8000/cmm/users/'
BATCH_GET_USER_INFO_URL = 'http://127.0.0.1:8000/cmm/users/info_list'
GET_USER_LIST_URL = 'http://127.0.0.1:8000/cmm/users/list'


DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bm',
        'USER': 'root',
        'PASSWORD': 'jj891030',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'benchmarks',
#         'USER': 'youdan',
#         'PASSWORD': 'Cangmami2017',
#         'HOST': 'rm-2ze07ui3391359lojo.mysql.rds.aliyuncs.com',
#         'PORT': '3306',
#     }
# }

# DATABASES = {
#     'default': {
#         # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'benchmarks',
#         'USER': 'aircos',
#         'PASSWORD': 'Aircos201710',
#         'HOST': 'rm-2ze2id33njw5c9414o.mysql.rds.aliyuncs.com',
#         'PORT': '3306',
#     }
# }

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
