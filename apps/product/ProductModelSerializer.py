from rest_framework.validators import UniqueValidator
from drf_haystack.serializers import HaystackSerializer
from apps.product.models import product
from rest_framework import serializers

from apps.product.search_index import productIndex


class ProductAddSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=100, required=True,allow_blank=False, error_messages={
        'allow_blank': '请输入产品名称',
        'max_length': '格式错误',

    }, validators=[UniqueValidator(queryset=product.objects.all(), message="产品名称已存在")])

    product_user = serializers.CharField(max_length=32, allow_blank=False, required=True,
                                         error_messages={'allow_blank': '请输入产品名称',
                                                         'max_length': '格式错误'})



    class Meta:
        model = product
        fields = ['product_name', 'product_desc', 'product_user']


class productListSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = "__all__"



class productIndexSerializer(HaystackSerializer):
    object = productListSerializer(read_only=True)

    class Meta:
        index_classes = [productIndex]
        fields = ('text', 'object')