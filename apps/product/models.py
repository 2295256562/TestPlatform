from django.db import models
import time
# Create your models here.
from apps.utils.deletemodel import SoftDeletableModel

shijiancuo = int(time.time())
class product(SoftDeletableModel, models.Model):
    product_name = models.CharField(max_length=100, blank=False, unique=True, verbose_name="产品名称")
    product_desc = models.CharField(max_length=100, blank=True, null=True, verbose_name="产品描述")
    product_user = models.CharField(max_length=32, blank=False, verbose_name="产品负责人")
    creater_time = models.IntegerField(default=shijiancuo, verbose_name="创建时间")


    class Meta:
        db_table = "products"
        verbose_name = "产品管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product_name

