# -*- coding: UTF-8 -*-
from django.db import models
from bm.models.base import BaseModel


# 分销商-商品-供应商关系
class ProdSupplierDistributor(BaseModel):
    distributor_id = models.IntegerField(null=False, db_index=True, verbose_name='分销商ID')
    product = models.ForeignKey('bm.Product', related_name='product', null=False, verbose_name='商品编码')
    supplier_id = models.CharField(max_length=40, null=False, verbose_name='供货商ID')
    is_like = models.NullBooleanField(default=False, verbose_name='是否收藏')
    is_sell = models.NullBooleanField(default=False, verbose_name='是否售卖')
    is_cart = models.NullBooleanField(default=False, verbose_name='是否加入商品库')

    class Meta:
        ordering = ['-created_at']
        db_table = 'prod_supplier_distributor'
