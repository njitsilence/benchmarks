#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by YangWei on 2018/5/31
from django.core.management import BaseCommand
from mysql_benchmarks.tests import test_connect_mysql

class Command(BaseCommand):


    def handle(self, *args, **options):

        print("---------统计完成--------------")

if __name__ == '__main__':
    pass
