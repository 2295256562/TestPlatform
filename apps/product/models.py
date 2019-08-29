from django.db import models
import time
# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=100, blank=False, verbose_name="产品名称")
    product_desc = models.CharField(max_length=100, blank=True, null=True, verbose_name="产品描述")
    product_user = models.CharField(max_length=32, blank=False, verbose_name="产品负责人")
    # creater_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    creater_time = models.IntegerField(default=int(time.time()), verbose_name="创建时间")
    is_del = models.BooleanField(default=False)

    class Meta:
        db_table = "tp_product"
        verbose_name = "产品管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product_name