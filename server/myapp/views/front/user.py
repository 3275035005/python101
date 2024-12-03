# Create your views here.
import datetime

from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import User
from myapp.serializers import UserSerializer

"""
    查询个人信息
"""
@api_view(['GET'])
def info(request):
    if request.method == 'GET':
        pk = request.GET.get('id', -1)
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

"""
    修改个人信息
"""
@api_view(['POST'])
def update(request):
    try:
        pk = request.data['id']
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    print(request.data)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        print(serializer.errors)
    return APIResponse(code=1, msg='更新失败')

"""
    余额充值
"""
@api_view(['POST'])
def rechargeAccount(request):
    try:
        pk = request.data['id']
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    data = request.data.copy()
    data.update({'account':  user.account + float(request.data['account'])})
    print(data)
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='充值成功', data=serializer.data)
    else:
        print(serializer.errors)
    return APIResponse(code=1, msg='充值失败')

