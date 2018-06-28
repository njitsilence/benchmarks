from django.test import TestCase

# Create your tests here.

from mongo_benchmarks.models import DevicePhotoModel
import traceback
from time import time
import os
from datetime import datetime
import pickle
import numpy as np
from log import Logger
import json
# 要遍历的根目录
rootdir = r'C:\180609'
resulst_dir = r'C:\bm_test\mongo'
# rootdir = r'C:\1'
log = Logger('insert_mongo.log', level='debug')


def read_pkl(path):
    """读取指定路径下的 PKL 数据, 返回 PKL 数组"""
    try:
        with open(path, 'rb') as fp:
            array_list = pickle.load(fp, encoding='latin')
        if len(list(filter(lambda array: not isinstance(array, np.ndarray), array_list))) > 0:
            log.logger.error("Record {} has unknown data".format(path))
            array_list = []
    except Exception as e:
        log.logger.error("Record {} read pkl error: {}".format(path, e))
        array_list = []

    return array_list


def _mongo_process_insert(path=None, label=None, feature=None):
    tb = time()
    try:
        DevicePhotoModel.objects.using('mysql').create(path=path, label=label, feature=feature)
    except Exception as e:
        print('插入失败，图片位置：{}'.format(path))
        print(str(e))
        traceback.print_exc()
    return time() - tb


def insert_into_mongo():
    i = 0
    j = 1
    insert_elapse_time_list = []
    insert_elapse_time_list_all = []
    insert_elapse_time_list_avg_per_10w = []
    # 遍历文件获取每张图片的路径
    print('开始插入mongo数据库的时间:{}'.format(datetime.now()))
    for fpath, dirs, fs in os.walk(rootdir):
        for f in fs:
            if f == '0.pkl':
                # 只处理0.pkl文件， 插入数据库
                pkl_path = os.path.join(fpath, f)
                label = np.random.randint(1, 20)
                ndarry_list = read_pkl(pkl_path)
                feature = pickle.dumps(ndarry_list)
                # 单条insert
                insert_elapse_time = _mongo_process_insert(path=pkl_path, label=label, feature=feature)
                insert_elapse_time_list.append(insert_elapse_time)
                insert_elapse_time_list_all.append(insert_elapse_time)
                i += 1
                if i % 1000 == 0:
                    fname = 'insert_elapse_time_' + str(j) + 'w'
                    fname_json = fname + '.json'
                    with open(os.path.join(resulst_dir, fname_json), 'w') as f:
                        # 每10w条记录的 平均insert时间
                        avg = np.array(insert_elapse_time_list).mean()
                        insert_elapse_time_list_avg_per_10w.append(avg)
                        res_dict = {fname: insert_elapse_time_list, 'insert_elapse_time_avg': avg}
                        f.write(json.dumps(res_dict))
                        insert_elapse_time_list = []
                        res_dict = {}
                        j += 1
                    print('已完成插入{}条数据----'.format(i))
    with open(os.path.join(resulst_dir, 'all_results.json'), 'w') as f:
        res_dict_all = {'insert_elapse_time_list': insert_elapse_time_list_all,
                        'insert_elapse_time_list_avg_per_10w': insert_elapse_time_list_avg_per_10w}
        f.write(json.dumps(res_dict_all))


    # log.logger.info('insert_elapse_time_list：{}'.format(insert_elapse_time_list))
    print('结束插入mongo数据库的时间:{}, 一共插入{}条记录'.format(datetime.now(), i))

















