# Create your views here.
from django.db import connection
from django.db.models import Q
from rest_framework.decorators import api_view, authentication_classes
from django.core.paginator import Paginator
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import ChargingStation
from myapp.permission.permission import isDemoAdminUser
from myapp.serializers import ChargingStationSerializer
from myapp.utils import dict_fetchall

"""
    查询充电站数据
"""
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        name = request.GET.get("name", '')
        classifications = ChargingStation.objects.filter(name__contains=name).order_by('-create_time')
        # 获取当前页码
        page = request.GET.get('page')
        # 实例化Paginator
        paginator = Paginator(classifications, 10)  # 每页显示10条记录
        page_obj = paginator.page(page)
        total = paginator.count  # 数据总条数
        serializer = ChargingStationSerializer(page_obj.object_list, many=True)

        data = {'list': serializer.data, 'total': total}
        return APIResponse(code=0, msg='查询成功', data=data)

"""
    查询充电站详情
"""
@api_view(['GET'])
def get_detail(request):
    if request.method == 'GET':
        id = request.GET.get("id", '')
        chargingStation = ChargingStation.objects.prefetch_related('station_id').get(id=id)
        serializer = ChargingStationSerializer(chargingStation)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
