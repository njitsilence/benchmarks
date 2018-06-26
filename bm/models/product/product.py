# -*- coding: UTF-8 -*-
from django.db import models
from bm.models.base import BaseModel
from bm.models.choices import SUPPLIER_PROD_SALE_STATUS_CHOICES, PROD_CHECK_STATUS_CHOICES


# 商品
class Product(BaseModel):
    product_id = models.CharField(
        max_length=40,
        primary_key=True,
        verbose_name='商品编码',
        editable=False)
    supplier_id = models.IntegerField(null=False, db_index=True, verbose_name='供货商ID')
    product_name = models.CharField(max_length=100, verbose_name='商品名称')
    product_detail = models.TextField(help_text=True, verbose_name='商品详情')
    product_sale_status = models.IntegerField(
        default=10,
        null=False,
        choices=SUPPLIER_PROD_SALE_STATUS_CHOICES,
        verbose_name='供应商商品销售状态')
    product_check_status = models.IntegerField(
        default=10,
        null=False,
        choices=PROD_CHECK_STATUS_CHOICES,
        verbose_name='商品审核状态')
    product_category = models.CharField(null=True, max_length=32, verbose_name='分类')
    product_sub_category = models.CharField(null=True, max_length=32, verbose_name='子分类')
    img_url_1 = models.URLField(null=True, verbose_name='主图')
    img_url_2 = models.URLField(null=True, verbose_name='图片地址2')
    img_url_3 = models.URLField(null=True, verbose_name='图片地址3')
    img_url_4 = models.URLField(null=True, verbose_name='图片地址4')
    img_url_5 = models.URLField(null=True, verbose_name='图片地址5')

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['-created_at']
        db_table = 'product'


# # 商品分类
# class Category(BaseModel):
#     category_id = models.AutoField(primary_key=True)
#     category_name = models.CharField(max_length=32,verbose_name='分类')
#     parent = models.ForeignKey('self',verbose_name='父分类',null=True,blank=True)
#
#     def __str__(self):
#         return self.category
#
#     class Meta:
#         ordering = ['-created_at']
#         db_table = 'category'

# 商品图片
# class ProductImg(BaseModel):
#     product_img_id = models.AutoField(primary_key=True, verbose_name='商品图片ID')
#     product = models.ForeignKey('bm.Product', related_name='product_img', null=True, verbose_name='商品ID')
#     img_url = models.URLField(null=True, verbose_name='图片地址')
#     is_main_img = models.BooleanField(default=False, verbose_name='是否主图')
#     seq = models.IntegerField(null=False, verbose_name='图片序号')
#
#     def __str__(self):
#         return self.img_url
#
#     class Meta:
#         ordering = ['-created_at']
#         db_table = 'product_img'