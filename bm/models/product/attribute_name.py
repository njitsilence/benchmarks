# -*- coding: UTF-8 -*-
from django.db import models
from bm.models.base import BaseModel


# 属性名
class AttributeName(BaseModel):
    attribute_name_id = models.AutoField(primary_key=True, verbose_name='属性名ID')
    attribute_name = models.CharField(max_length=100, verbose_name='属性名')
    allow_alias = models.BooleanField(default=False, verbose_name='是否允许别名')
    is_color = models.BooleanField(default=False, verbose_name='是否颜色属性')
    is_size = models.BooleanField(default=False, verbose_name='是否尺寸属性')
    is_weight = models.BooleanField(default=False, verbose_name='是否重量属性')
    is_enum = models.BooleanField(default=False, verbose_name='是否枚举属性')
    is_input = models.BooleanField(default=False, verbose_name='是否输入属性')
    is_key = models.BooleanField(default=False, verbose_name='是否关键属性')
    is_sale = models.BooleanField(default=False, verbose_name='是否销售属性')
    is_search = models.BooleanField(default=False, verbose_name='是否搜索属性')
    is_must = models.BooleanField(default=False, verbose_name='是否必须')
    is_multiple_choice = models.BooleanField(default=False, verbose_name='是否多选')

    def __str__(self):
        return self.attribute_name

    class Meta:
        ordering = ['-created_at']
        db_table = 'attribute_name'
