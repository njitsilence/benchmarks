# -*- coding: UTF-8 -*-
from django.db import models
from bm.models.base import BaseModel


# 属性值
class AttributeValue(BaseModel):
    attribute_value_id = models.AutoField(primary_key=True, verbose_name='属性值ID')
    attribute_value = models.CharField(max_length=100, verbose_name='属性值')
    attribute_name_id = models.ForeignKey('bm.AttributeName', null=True, verbose_name='属性名')
    status = models.IntegerField(default=10, null=False, verbose_name='属性值状态')
    seq = models.IntegerField(null=False, verbose_name='序号')

    def __str__(self):
        return self.attribute_value

    class Meta:
        ordering = ['-created_at']
        db_table = 'attribute_value'
