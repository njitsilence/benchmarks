#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by YangWei on 2018/5/31
from django.core.management import BaseCommand
from mysql_benchmarks.tests import select_mysql


class Command(BaseCommand):

    help = "查询mysql"

    def handle(self, *args, **options):
        select_mysql()
        print("---------查询mysql完成--------------")


if __name__ == '__main__':
    pass
