from django.conf.locale import es
from django.http import HttpResponse
from django.test import TestCase

import time
from django.db import models
from elasticsearch import helpers
from rest_framework.decorators import action

from apps.product.models import product
print(int(time.time()))
print(type(int(time.time())))


def es2(request):
    query_obj = product.objects.all()
    print(query_obj)
    action = (
        {
            "_index": "s18",
            "_type": "doc",
            "_source": {
                "title": i.title,
                "summary": i.summary,
                "a_url": i.a_url,
                "img_url": i.img_url,
                "tags": i.tags

            }
        } for i in query_obj)
# print(action, next(action))
    import time

    s = time.time()

    helpers.bulk(es, action)
    print(time.time() - s)

    return HttpResponse('OK')
