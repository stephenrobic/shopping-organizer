from django.urls import path
from . import views

app_name = 'shopping_list'
urlpatterns = [
    # ex: /
    path('', views.home, name='home'),
    # ex: /create_list
    path('create_list/', views.create_list, name='create_list'),
    # path('creating_list/', views.creating_list, name='creating_list'),
    # ex: /5
    path('create_list/list_details/<int:list_id>/', views.list_details, name='list_details')
]
