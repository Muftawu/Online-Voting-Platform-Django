from django.urls import path 
from . import views

app_name = 'voting'

urlpatterns = [
    path('ballot/', views.vote, name='vote'),
    path('dashboard/', views.voter_dashboard, name='voter_dashboard'),
]