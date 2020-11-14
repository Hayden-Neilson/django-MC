from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('item/', views.index,name='item'),
    path('<int:item_id>/', views.detail,name='detail/'),
]