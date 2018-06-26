# -*- coding: UTF-8 -*-
from django.db import models
from bm.models.base import BaseModel


# 商品属性
class SkuBasicAttribute(BaseModel):
    id = models.AutoField(primary_key=True)
    sku_id = models.ForeignKey('bm.Sku', null=True, verbose_name='sku编码')
    product_id = models.ForeignKey('bm.Product', null=True, verbose_name='商品ID')
    attribute_name_id = models.ForeignKey('bm.AttributeName', null=True, verbose_name='属性名')
    attribute_value_id = models.ForeignKey('bm.AttributeValue', null=True, verbose_name='属性值')

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['-created_at']
        db_table = 'sku_basic_attribute'
