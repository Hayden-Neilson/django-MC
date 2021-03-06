from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.index,name='index'),
    path('item/', views.index,name='item'),
    path('<int:item_id>/', views.detail,name='detail/'),
    path ('add',views.create_item,name='create_item')
    path ('update',views.update_item,name='update_item')
]