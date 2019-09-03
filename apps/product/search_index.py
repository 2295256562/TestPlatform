from haystack import indexes
from apps.product.models import product

class productIndex(indexes.SearchIndex, indexes.Indexable):
    # document=True  说明text字段是索引字段
    # use_template:表示通过模板文件来指定该字段的索引由哪些模型字段组成
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """返回索引类对应模型类"""
        return product

    def index_queryset(self, using=None):
        """返回要建立索引数据的查询集"""
        return self.get_model().objects.all()