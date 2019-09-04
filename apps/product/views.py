from django.http import JsonResponse
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from drf_haystack.viewsets import HaystackViewSet
from apps.product.models import product
from apps.utils.custom_viewset_base import CustomViewBase
from apps.product.ProductModelSerializer import ProductAddSerializer, productListSerializer, productIndexSerializer
from apps.utils.custom_pagination import PageResultsSetPagination


class productSearchView(HaystackViewSet):
    index_models = [product]
    serializer_class = productIndexSerializer


class ProductList(CustomViewBase):
    """产品列表页"""
    # permission_classes = (IsAuthenticated,)
    queryset = product.objects.filter(is_deleted=False).order_by('id')
    pagination_class = PageResultsSetPagination
    serializer_class = productListSerializer


class ProductAdd(CustomViewBase):
    """新增产品"""
    serializer_class = ProductAddSerializer
    queryset = product.objects.all()




