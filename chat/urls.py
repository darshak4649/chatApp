from django.urls import path
from . import views

urlpatterns = [
    path('', views.chats, name= 'chats'),
    path('create_user/', views.create_user, name='create_user'),
    path('chat/<str:user_id>/', views.user_chat, name='user_chat'),
    
]
