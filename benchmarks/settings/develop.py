# -*- coding:utf-8 -*-

from .base import *

DEBUG = True

APP_CENTER_URL = 'http://dev.api.aircos.com/open'
GET_USER_INFO_URL = 'http://dev.api.aircos.com/cmm/users/'
BATCH_GET_USER_INFO_URL = 'http://dev.api.aircos.com/cmm/users/info_list'
GET_USER_LIST_URL = 'http://dev.api.aircos.com/cmm/users/list'

GET_MATCHED_STATION_LIST_URL = \
    'http://dev.api.aircos.com/accounting/express/v1.2/warehouses/match_station_list'
GET_STATION_INFO_URL = \
    'http://dev.api.aircos.com/accounting/express/v1.2/stations/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'benchmarks',
        'USER': 'root',
        'PASSWORD': 'Xbm201512',
        'HOST': 'rm-2zec5io6m85842bx2zo.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    }
}
REDIS_CONFIG = {
    'orderjob': {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 7218,
        'REDIS_DB': '0',
        'REDIS_PASSWORD': 'YcMi@7@lVroX@d6ewmE+@83o3Cj#rf'
    },
    'raw_order': {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 7218,
        'REDIS_DB': '1',
        'REDIS_PASSWORD': 'YcMi@7@lVroX@d6ewmE+@83o3Cj#rf'
    },
    'log_server': {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 7218,
        'REDIS_DB': '2',
        'REDIS_PASSWORD': 'YcMi@7@lVroX@d6ewmE+@83o3Cj#rf'
    },
    'default': {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 7218,
        'REDIS_DB': '3',
        'REDIS_PASSWORD': "YcMi@7@lVroX@d6ewmE+@83o3Cj#rf"
    },
    'user': {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 7218,
        'REDIS_DB': '4',
        'REDIS_PASSWORD': 'YcMi@7@lVroX@d6ewmE+@83o3Cj#rf'
    },

}
MQ_CONFIG = {
    'log_server': {
        'HOST': "47.93.203.234",
        'PORT': 5672,
        'USERNAME': 'benchmarks',
        'PASSWORD': "cmmpassword"
    },
    'default': {
        'SERVER': '127.0.0.1',
        'PORT': 5672,
        'VHOST': '/',
        'USER': 'guest',
        'PASSWORD': 'guest',
    }
}
