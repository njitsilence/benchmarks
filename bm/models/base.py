from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.NullBooleanField(default=False, verbose_name='是否删除')

    class Meta:
        abstract = True
        ordering = ['-created_at']