#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by YangWei on 2018/5/31
from django.core.management import BaseCommand
from mysql_benchmarks.tests import insert_into_mysql


class Command(BaseCommand):

    help = "插入mysql"

    def handle(self, *args, **options):
        insert_into_mysql()
        print("---------插入mysql完成--------------")


if __name__ == '__main__':
    pass
