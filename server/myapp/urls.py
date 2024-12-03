from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    # api

    path('manage/chargingStation/list', views.manage.chargingStation.list_api),
    path('manage/chargingStation/create', views.manage.chargingStation.create),
    path('manage/chargingStation/update', views.manage.chargingStation.update),
    path('manage/chargingStation/delete', views.manage.chargingStation.delete),
    path('manage/chargingStation/getList', views.manage.chargingStation.get_list),


    path('manage/chargingPile/list', views.manage.chargingPile.list_api),
    path('manage/chargingPile/create', views.manage.chargingPile.create),
    path('manage/chargingPile/update', views.manage.chargingPile.update),
    path('manage/chargingPile/delete', views.manage.chargingPile.delete),

    path('manage/notice/list', views.manage.notice.list_api),
    path('manage/notice/create', views.manage.notice.create),
    path('manage/notice/update', views.manage.notice.update),
    path('manage/notice/delete', views.manage.notice.delete),
    path('manage/notice/getList', views.manage.notice.get_list),

    path('manage/banner/list', views.manage.banner.list_api),
    path('manage/banner/create', views.manage.banner.create),
    path('manage/banner/update', views.manage.banner.update),
    path('manage/banner/delete', views.manage.banner.delete),

    path('manage/user/admin_login', views.manage.user.admin_login),
    path('manage/user/list', views.manage.user.list_api),
    path('manage/user/create', views.manage.user.create),
    path('manage/user/resetPassword', views.manage.user.resetPassword),

    path('manage/user/update', views.manage.user.update),
    path('manage/user/delete', views.manage.user.delete),
    path('manage/user/info', views.manage.user.info),


    path('manage/order/list', views.manage.order.list_api),
    path('manage/order/delete', views.manage.order.delete),
    path('manage/feedback/list', views.manage.feedback.list_api),
    path('manage/feedback/update', views.manage.feedback.update),
    path('manage/feedback/delete', views.manage.feedback.delete),
    path('manage/file/upload', views.manage.file.upload),


    path('front/banner/get_list', views.front.banner.get_list),
    path('front/chargingStation/list_api', views.front.chargingStation.list_api),
    path('front/chargingStation/get_detail', views.front.chargingStation.get_detail),

    path('front/order/list_api', views.front.order.list_api),
    path('front/order/update', views.front.order.update),

    path('front/user/info', views.front.user.info),
    path('front/user/update', views.front.user.update),
    path('front/user/rechargeAccount', views.front.user.rechargeAccount),

    path('front/feedback/list_api', views.front.feedback.list_api),
    path('front/feedback/create', views.front.feedback.create),

    path('front/chargingPilePrice/list_api', views.front.chargingPilePrice.list_api),
]
