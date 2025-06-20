from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginPageUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
