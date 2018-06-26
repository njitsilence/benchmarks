# -*- coding: UTF-8 -*-
from django.db import models
from bm.models.base import BaseModel


# 商品sku
class Sku(BaseModel):
    sku_id = models.CharField(
        max_length=40,
        primary_key=True,
        verbose_name='Sku编码',
        editable=False)
    sku_name = models.CharField(max_length=128, db_index=True, verbose_name='sku名称')
    supply_price = models.FloatField(null=True, default=0.0, verbose_name='供货价格')
    outer_item_code = models.CharField(null=True, max_length=64, verbose_name='商家编码')
    available_quantity = models.IntegerField(null=True, default=0, verbose_name='可用Sku数量')
    distribution_limit_pct = models.IntegerField(null=True, default=0, verbose_name='分销上限百分比')
    safety_stock_percent = models.IntegerField(null=True, default=0, verbose_name='安全库存百分比')
    product = models.ForeignKey('bm.Product', null=True, verbose_name='商品ID')

    def __str__(self):
        return self.sku_name

    class Meta:
        ordering = ['-created_at']
        db_table = 'sku'



