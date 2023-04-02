from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('sign-up/', views.sign_up_page, name='sign_up'),
    path('logout/', views.logout_page, name='logout'),
]