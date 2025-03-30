from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),						#通过url设置对应的映射
    path('ask/', views.ask, name='ask'),  # 确保这条路由存在
]
