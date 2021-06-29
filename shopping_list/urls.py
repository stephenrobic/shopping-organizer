from django.urls import path
from . import views

app_name = 'shopping_list'
urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /5
    path('<int:list_id>/', views.detail, name='detail')
]
