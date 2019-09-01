from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from collections import OrderedDict
from rest_framework.response import Response

# 分页插件

class LargeResultsSetPagination(LimitOffsetPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        code = 200
        msg = 'success'
        if not data:
            # code = 404
            msg = "Data Not Found"

        return Response(OrderedDict([
            ('code', code),
            ('msg', msg),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('data', data),
        ]))


class PageResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        code = 200
        msg = 'success'
        if not data:
            # code = 404
            msg = "Data Not Found"
        if msg == 'success':
            return Response(OrderedDict([
                ('code', code),
                ('msg', msg),
                ('count', self.page.paginator.count),
                ('next', self.get_next_link()),
                ('previous', self.get_previous_link()),
                ('data', data),
            ]))
        else:
            return Response(OrderedDict([
                ('code', code),
                ('msg', msg),
                ('data', []),
            ]))
