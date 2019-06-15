from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('create_user', views.UserRegister.as_view(), name='create_user'),
    path('users_list',  views.UsersListView.as_view(), name='users_list'),
]