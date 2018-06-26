# -*- coding: UTF-8 -*-
from django.db import models
from bm.models.base import BaseModel
from bm.models.choices import INVENTORY_TYPE


# 库存
class Inventory(BaseModel):
    id = models.AutoField(primary_key=True)
    warehouse_id = models.CharField(
        max_length=20,
        null=True,
        verbose_name='仓库id')
    warehouse_name = models.CharField(
        max_length=32,
        null=True,
        verbose_name='仓库名称')
    product_id = models.ForeignKey('bm.Product', null=True, verbose_name='商品ID')
    sku_id = models.ForeignKey('bm.Sku', null=True, verbose_name='商品Sku编码')
    inventory_type = models.CharField(
        max_length=20,
        choices=INVENTORY_TYPE,
        verbose_name='库存类型', default=INVENTORY_TYPE[0][0])
    available_qty = models.IntegerField(null=True, verbose_name='可用库存')
    user_id = models.CharField(
        max_length=30,
        verbose_name='所有者id', null=True)
    operator_id = models.CharField(
        max_length=30,
        verbose_name='操作者id', default='system')

    class Meta:
        ordering = ['-created_at']
        db_table = 'inventory'
