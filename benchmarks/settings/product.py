# -*- coding:utf-8 -*-

from .base import *

DEBUG = False

# APP_CENTER = {
#     "ip": "47.95.235.167",
#     "port": 8003
# }
# APP_CENTER_URL = 'api.open.aircos.com'
APP_CENTER_URL = 'https://api.aircos.com/open'
GET_USER_INFO_URL = 'https://api.aircos.com/cmm/users/'
BATCH_GET_USER_INFO_URL = 'http://api.aircos.com/cmm/users/info_list'
GET_USER_LIST_URL = 'https://api.aircos.com/cmm/users/list'
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bm',
        'USER': 'aircos',
        'PASSWORD': 'Aircos201710',
        # 'HOST': 'rm-2ze2id33njw5c9414.mysql.rds.aliyuncs.com',
        'HOST': 'rm-2zei290y0jssy27y5po.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    }
}

GET_MATCHED_STATION_LIST_URL = \
    'https://api.aircos.com/accounting/express/v1.2/warehouses/match_station_list'
GET_STATION_INFO_URL = \
    'https://api.aircos.com/accounting/express/v1.2/stations/'

REDIS_CONFIG = {
    # orderjob任务队列
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
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 6379,
        'REDIS_DB': '4',
        'REDIS_PASSWORD': ""
    },

}
MQ_CONFIG = {
    'log_server': {
        'HOST': "39.106.175.187",
        'PORT': 5672,
        'USERNAME': 'benchmarks',
        'PASSWORD': "cmmpassword"
    },
    'default': {
        'SERVER': '39.106.175.187',
        'PORT': 5762,
        'VHOST': '/',
        'USER': 'benchmarks',
        'PASSWORD': 'cmmpassword',
    }
}
