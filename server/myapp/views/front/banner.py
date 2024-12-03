# Create your views here.
from django.db import connection
from django.db.models import Q
from rest_framework.decorators import api_view, authentication_classes
from django.core.paginator import Paginator
from myapp.handler import APIResponse
from myapp.models import Banner
from myapp.serializers import BannerSerializer

"""
    查询首页轮播图列表
"""
@api_view(['GET'])
def get_list(request):
    if request.method == 'GET':
        notice = Banner.objects.all().order_by('-create_time')
        serializer = BannerSerializer(notice, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
