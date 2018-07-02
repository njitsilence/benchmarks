#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by YangWei on 2018/5/31
from django.core.management import BaseCommand
from mongo_benchmarks.tests import select_mongo


class Command(BaseCommand):

    help = "查询mongo"

    def handle(self, *args, **options):
        select_mongo()
        print("---------查询mongo完成--------------")


if __name__ == '__main__':
    pass
