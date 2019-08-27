from rest_framework.validators import UniqueValidator

from apps.product.models import product
from rest_framework import serializers


class ProductAddSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=100, required=True, allow_blank=False, error_messages={
        'allow_blank': '请输入产品名称',
        'max_length': '格式错误'
    }, validators=[UniqueValidator(queryset=product.objects.filter(is_del=False), message="产品名称已存在")])

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
