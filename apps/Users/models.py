import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    用户模型类
    """
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    uqdate_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = "tp_users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name