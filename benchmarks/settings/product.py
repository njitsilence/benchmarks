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
        'PASSWORD': 'mysql123',
        'HOST': '192.168.3.99',
        'PORT': '3306',
    },
    'psql': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bm',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '192.168.3.99',
        'PORT': '5432',
    },
    'mongo': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'djongo',
        'NAME': 'bm',
        # 'NAME': 'bm',
        'HOST': '192.168.3.99',
        'PORT': 27017,
    }
}

GET_MATCHED_STATION_LIST_URL = \
    'http://test.api.aircos.com/accounting/express/v1.2/warehouses/match_station_list'
GET_STATION_INFO_URL = \
    'http://test.api.aircos.com/accounting/express/v1.2/stations/'

REDIS_CONFIG = {
    # orderjob任务队列
    'orderjob': {
        # 'REDIS_HOST': '47.95.235.167',
        'REDIS_HOST': "127.0.0.1",
        'REDIS_PORT': 7218,
        'REDIS_DB': '0',
        'REDIS_PASSWORD': "YcMi@7@lVroX@d6ewmE+@83o3Cj#rf"
    },
    'raw_order': {
        'REDIS_HOST': "127.0.0.1",
        'REDIS_PORT': 7218,
        'REDIS_DB': '1',
        'REDIS_PASSWORD': "YcMi@7@lVroX@d6ewmE+@83o3Cj#rf"
    },
    'log_server': {
        'REDIS_HOST': "127.0.0.1",
        'REDIS_PORT': 7218,
        'REDIS_DB': '2',
        'REDIS_PASSWORD': "YcMi@7@lVroX@d6ewmE+@83o3Cj#rf"
    },
    'default': {
        'REDIS_HOST': "127.0.0.1",
        'REDIS_PORT': 7218,
        'REDIS_DB': '3',
        'REDIS_PASSWORD': "YcMi@7@lVroX@d6ewmE+@83o3Cj#rf"
    },
    'user': {
        'REDIS_HOST': "test.xbmhz.com",
        'REDIS_PORT': 7218,
        'REDIS_DB': '4',
        'REDIS_PASSWORD': "YcMi@7@lVroX@d6ewmE+@83o3Cj#rf"
    },
}

MQ_CONFIG = {
    'log_server': {
        'HOST': "47.94.102.146",
        'PORT': 5672,
        'USERNAME': 'benchmarks',
        'PASSWORD': "cmmpassword"
    },
    'default': {
        'SERVER': '47.94.102.146',
        'PORT': 5762,
        'VHOST': '/',
        'USER': 'benchmarks',
        'PASSWORD': 'cmmpassword',
    }
}
