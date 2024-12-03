# Create your views here.
from rest_framework.decorators import api_view
from myapp.handler import APIResponse
from myapp.models import ChargingPilePrice
from myapp.serializers import ChargingPilePriceSerializer

"""
    查询充电站数据
"""


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        pileId = request.GET.get("id", '')
        classifications = ChargingPilePrice.objects.filter(pile_id=pileId).order_by('-hour')
        serializer = ChargingPilePriceSerializer(classifications, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
