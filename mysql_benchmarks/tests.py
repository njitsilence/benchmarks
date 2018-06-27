from django.test import TestCase

# Create your tests here.

from mysql_benchmarks.models import DevicePhotoModel


def test_connect_mysql():

    res = DevicePhotoModel.objects.using('mysql').all()

    return res.count()

import pickle
import numpy as np


def read_pkl(path):
    """读取指定路径下的 PKL 数据, 返回 PKL 数组"""
    try:
        with open(path, 'rb') as fp:
            array_list = pickle.load(fp, encoding='latin')
        if len(list(filter(lambda array: not isinstance(array, np.ndarray), array_list))) > 0:
            # logger.error("Record {} has unknown data".format(path))
            array_list = []

    except Exception as e:
        # logger.error("Record {} read pkl error: {}".format(path, e))
        array_list = []

    return array_list



import os
from datetime import datetime
# 要遍历的根目录
rootdir = r'C:\180609'



def insert_into_():
    i = 0
    # 遍历文件获取每张图片的路径
    print('开始插入mysql数据库的时间:{}'.format(datetime.now()))
    for fpath, dirs, fs in os.walk(rootdir):
        for f in fs:
            if f == '0.pkl':
                # 只处理0.pkl文件， 插入数据库
                pkl_path=os.path.join(fpath, f)
                # 单条insert
                # mysql_process_insert()




            i += 1
    print('结束插入mysql数据库的时间:{}, 一共插入{}条记录'.format(datetime.now(), i))



def mysql_process_insert():
    return 123













