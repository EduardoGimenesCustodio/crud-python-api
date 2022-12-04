from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('user/', views.UserDetail.as_view(), name='user-detail'),
    path('graph/bar/', views.generate_bar_graph, name='bar-graph')
]