#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by YangWei on 2018/5/31
from django.core.management import BaseCommand
from mongo_benchmarks.tests import insert_into_mongo


class Command(BaseCommand):

    help = "插入mongo"

    def handle(self, *args, **options):
        insert_into_mongo()
        print("---------插入mongo完成--------------")


if __name__ == '__main__':
    pass
