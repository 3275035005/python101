# Create your views here.
from django.db import connection
from django.db.models import Q
from rest_framework.decorators import api_view, authentication_classes
from django.core.paginator import Paginator
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Feedback
from myapp.models import User
from myapp.permission.permission import isDemoAdminUser
from myapp.serializers import FeedbackSerializer
from myapp.utils import dict_fetchall

"""
    查询数据
"""
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        userId = request.GET.get("userId", '')
        query = Q()
        query &= Q(user_id=userId)
        classifications = Feedback.objects.filter(query).order_by('-create_time')
        serializer = FeedbackSerializer(classifications, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


"""
    提交反馈
"""
@api_view(['POST'])
def create(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='提交成功')

    return APIResponse(code=1, msg='提交失败')
