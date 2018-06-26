# -*- coding:utf-8 -*-

from .base import *

DEBUG = True

# APP_CENTER = {
#     "ip": "47.95.235.167",
#     "port": 8003
# }
# APP_CENTER_URL = 'test.api.open.aircos.com'
APP_CENTER_URL = 'http://test.api.aircos.com/open'
GET_USER_INFO_URL = 'http://test.api.aircos.com/cmm/users/'
BATCH_GET_USER_INFO_URL = 'http://test.api.aircos.com/cmm/users/info_list'
GET_USER_LIST_URL = 'http://test.api.aircos.com/cmm/users/list'
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bm',
        'USER': 'youdan',
        'PASSWORD': 'Cangmami2017',
        'HOST': 'rm-2ze07ui3391359lojo.mysql.rds.aliyuncs.com',
        'PORT': '3306',
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
