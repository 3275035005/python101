from rest_framework import serializers

"""
    序列化层
"""
## 新增
from myapp.models import ChargingStation, Notice, ChargingPile, ChargingPilePrice, Order, Feedback, File, User ,  Banner\


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


# 新增数据
class NoticeSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Notice
        fields = '__all__'


class ChargingPilePriceSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = ChargingPilePrice
        fields = '__all__'


class ChargingPileSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    # 额外字段
    name = serializers.ReadOnlyField(source='station.name')

    children = ChargingPilePriceSerializer(many=True, read_only=True)

    class Meta:
        model = ChargingPile
        fields = '__all__'
        # fields = ['id', 'number', 'type', 'state', 'name', 'create_time']


# 新增数据
class ChargingStationSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    station_id = ChargingPileSerializer(many=True, read_only=True)

    class Meta:
        model = ChargingStation
        fields = '__all__'



class BannerSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Banner
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = User
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    # 额外字段
    number = serializers.ReadOnlyField(source='pile.number')
    name = serializers.ReadOnlyField(source='pile.station.name')
    type = serializers.ReadOnlyField(source='pile.type')
    user_name = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Order
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    user_name = serializers.ReadOnlyField(source='user.name')
    class Meta:
        model = Feedback
        fields = '__all__'


