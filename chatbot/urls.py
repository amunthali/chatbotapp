from django.urls import path
from .views import register, chat, chat_history, user_login, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('', chat, name='chat'),
    path('chat/history/', chat_history, name='chat_history'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]