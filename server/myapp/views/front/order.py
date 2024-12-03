# Create your views here.
from django.db import connection
from django.db.models import Q
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from myapp.handler import APIResponse
from myapp.models import Order, User, ChargingPile, ChargingPilePrice
from myapp.serializers import OrderSerializer, UserSerializer
from myapp.utils import dict_fetchall
from myapp import utils


"""
    查询我的订单
"""
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        userId = request.GET.get("userId", '')
        state = request.GET.get("state", '')
        query = Q()
        query &= Q(user_id=userId)
        query &= Q(state__contains=state)
        classifications = Order.objects.filter(query).all().order_by('-create_time')
        # 获取当前页码
        page = request.GET.get('page')
        # 实例化Paginator
        paginator = Paginator(classifications, 10)  # 每页显示10条记录
        page_obj = paginator.page(page)
        total = paginator.count  # 数据总条数
        serializer = OrderSerializer(page_obj.object_list, many=True)
        data = {'list': serializer.data, 'total': total}
        return APIResponse(code=0, msg='查询成功', data=data)


"""
    取消充电
"""
@api_view(['POST'])
def update(request):
    try:
        pk = request.data['id']
        classification = Order.objects.get(id=pk, state='0')
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='充电已完成，无法取消')

    serializer = OrderSerializer(classification, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='取消成功')

    return APIResponse(code=1, msg='取消失败')


"""
    立即充电
"""
@api_view(['POST'])
def charge(request):

    pileId = request.data['pileId']
    priceId = request.data['priceId']
    userId = request.data['userId']
    # 1、判断充电桩是否使用
    try:
        chargingPile = ChargingPile.objects.get(id=pileId, state='2')
    except ChargingPile.DoesNotExist:
        return APIResponse(code=1, msg='充电桩无法使用')
    # 2、查询充电桩资金
    try:
        chargingPilePrice = ChargingPilePrice.objects.get(id=priceId)
    except ChargingPilePrice.DoesNotExist:
        return APIResponse(code=1, msg='价格获取失败')

    try:
        user = User.objects.get(id=userId)
    except User.DoesNotExist:
        return APIResponse(code=1, msg='用户获取失败')

    if chargingPilePrice.price > user.account:
        return APIResponse(code=1, msg='余额不足')

    # 3、扣除用户余额
    user.update({'account': user.account - chargingPilePrice.price})
    userSerializer = UserSerializer(user)
    if userSerializer.is_valid():
        userSerializer.save()

    # 4、新增订单
    data = request.data.copy()
    data.update({'money': chargingPilePrice.price,
                 'hour': chargingPilePrice.hour,
                 'start_charging_time': utils.get_day(),
                 'end_charging_time': utils.get_day_add_hour(chargingPilePrice.hour)})

    orderSerializer = OrderSerializer(data=data)
    if orderSerializer.is_valid():
        orderSerializer.save()
        return APIResponse(code=0, msg='充电成功')

    return APIResponse(code=1, msg='充电失败')

