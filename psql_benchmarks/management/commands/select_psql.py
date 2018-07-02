#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by YangWei on 2018/5/31
from django.core.management import BaseCommand
from psql_benchmarks.tests import select_psql


class Command(BaseCommand):

    help = "查询psql"

    def handle(self, *args, **options):
        select_psql()
        print("---------查询psql完成--------------")


if __name__ == '__main__':
    pass
