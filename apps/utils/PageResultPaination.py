from rest_framework.pagination import PageNumberPagination


class TestPage(PageNumberPagination):
    """分页配置"""
    page_size = 10   # 默认每页显示个数
    page_query_param = "page_index"   # 页码参数
    page_size_query_param = 'page_size'
    max_page_size = 100
