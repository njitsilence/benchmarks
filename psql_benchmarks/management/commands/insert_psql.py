#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by YangWei on 2018/5/31
from django.core.management import BaseCommand
from psql_benchmarks.tests import insert_into_psql


class Command(BaseCommand):

    help = "插入psql"

    def handle(self, *args, **options):
        insert_into_psql()
        print("---------插入psql完成--------------")


if __name__ == '__main__':
    pass
