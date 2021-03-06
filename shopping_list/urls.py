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
    path('list_details/<int:list_id>/', views.list_details, name='list_details'),

    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    path('add_friend/', views.add_friend, name="add_friend"),
    path('add_friend/<int:request_id>/', views.add_friend, name="add_friend"),
    path('add_friend/<str:friend_name>/', views.add_friend, name="add_friend")
]
