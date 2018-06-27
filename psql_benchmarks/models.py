from django.db import models
from datetime import datetime


# 用于基准测试剔除了外键 device和cluster
class DevicePhotoModel(models.Model):
    """
    设备上传图像信息表
    """
    id = models.BigAutoField(primary_key=True)
    # device = models.ForeignKey(DeviceInfoModel, verbose_name='设备名')
    upload_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')
    take_photo_time = models.DateTimeField(verbose_name='抓拍时间', db_index=True)
    path = models.CharField(max_length=100, verbose_name='存放路径')
    label = models.IntegerField(default=-1, verbose_name='聚类特征值')
    feature = models.BinaryField(null=True, default=None, verbose_name='特征向量数组')
    # cluster = models.ForeignKey('PhotoClusterModel', null=True, default=None, on_delete=models.SET_NULL,
    #                             verbose_name='类别')

    class Meta:
        verbose_name = "图像信息"
        verbose_name_plural = verbose_name
        db_table = 'device_photo'
        app_label = 'psql_benchmarks'
        ordering = ['-take_photo_time']

    def __str__(self):
        return '[{} {}] {}'.format(self.take_photo_time.strftime('%y-%m-%d %H:%M:%S'), self.device.name, self.id)
