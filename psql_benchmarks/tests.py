from django.test import TestCase

# Create your tests here.

from psql_benchmarks.models import DevicePhotoModel
import traceback
from time import time
import os
from datetime import datetime
import pickle
import numpy as np
from log import Logger
import json
from bm.ndarry_list import ndarry_list
# 要遍历的根目录
rootdir = r'C:\180609'
resulst_dir = r'C:\bm_test_hi\psql'
# rootdir = r'C:\1'
log = Logger('insert_psql.log', level='debug')


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


def _psql_process_insert(path=None, label=None, feature=None):
    tb = time()
    try:
        DevicePhotoModel.objects.using('psql').create(path=path, label=label, feature=feature)
    except Exception as e:
        print('插入失败，图片位置：{}'.format(path))
        print(str(e))
        traceback.print_exc()
    return time() - tb


def insert_into_psql():
    i = 0
    j = 1
    insert_elapse_time_list = []
    insert_elapse_time_list_all = []
    insert_elapse_time_list_avg_per_10w = []
    # 遍历文件获取每张图片的路径
    print('开始插入psql数据库的时间:{}'.format(datetime.now()))
    for _ in range(1000000):
    # for fpath, dirs, fs in os.walk(rootdir):
    #     for f in fs:
    #         if f == '0.pkl':
    #             # 只处理0.pkl文件， 插入数据库
    #             pkl_path = os.path.join(fpath, f)
        label = np.random.randint(1, 20)
        # ndarry_list = read_pkl(pkl_path)
        feature = pickle.dumps(ndarry_list)
        # 单条insert
        insert_elapse_time = _psql_process_insert(path='path', label=label, feature=feature)
        insert_elapse_time_list.append(insert_elapse_time)
        insert_elapse_time_list_all.append(insert_elapse_time)
        i += 1
        if i % 100000 == 0:
            fname = 'insert_elapse_time_' + str(j) + '0w'
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
    print('结束插入psql数据库的时间:{}, 一共插入{}条记录'.format(datetime.now(), i))








def _psql_process_select(label):
    tb = time()
    try:
        res = DevicePhotoModel.objects.all().using('psql').filter(label__in=label)
        count = res.count()
    except Exception as e:
        print('psql查询失败：{}')
        print(str(e))
        traceback.print_exc()
    return time() - tb, count



def select_psql():
    l2 = []
    l4 = []
    l6 = []
    l8 = []
    print('开始查询psql数据库的时间:{}'.format(datetime.now()))
    for _ in range(50):

        res20w_time, _ = _psql_process_select([1, 2, 3, 4])
        res40w_time, _ = _psql_process_select([5, 6, 7, 8, 9, 10, 11, 12])
        res60w_time, _ = _psql_process_select([13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5])
        res80w_time, c = _psql_process_select([19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4])
        l2.append(res20w_time)
        l4.append(res40w_time)
        l6.append(res60w_time)
        l8.append(res80w_time)
    d_l2 = np.array(l2).mean()
    d_l4 = np.array(l4).mean()
    d_l6 = np.array(l6).mean()
    d_l8 = np.array(l8).mean()

    print(d_l2,d_l4,d_l6,d_l8)

    print('结束查询psql数据库的时间:{}'.format(datetime.now()))








