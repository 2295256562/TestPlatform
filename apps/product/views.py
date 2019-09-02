from django.http import JsonResponse
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated

from apps.product.models import product
from apps.utils.custom_viewset_base import CustomViewBase
from apps.product.ProductModelSerializer import ProductAddSerializer, productListSerializer
from apps.utils.custom_pagination import PageResultsSetPagination

class GoodsPagination(PageNumberPagination):
    """
    商品列表自定义分页
    """
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class ProductList(CustomViewBase):
    """产品列表页"""
    # permission_classes = (IsAuthenticated,)
    queryset = product.objects.filter(is_del=False).order_by('id')
    pagination_class = PageResultsSetPagination
    serializer_class = productListSerializer


class ProductAdd(CustomViewBase):
    """新增产品"""
    serializer_class = ProductAddSerializer
    queryset = product.objects.all()




