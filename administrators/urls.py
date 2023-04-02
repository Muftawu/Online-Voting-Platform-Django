from django.urls import path 
from . import views

app_name = 'administrators'

urlpatterns = [
     path('', views.admin_dashboard, name='admin_dashboard'),
    
    path('admin-positions-view/', views.adminPositionsView, name='adminPositionsView'),
    path('admin-candidates-view/',views.adminCandidatesView, name='adminCandidatesView'),
    path('admin-voters-view/', views.adminVotersView, name='adminVotersView'),
    path('admin-voted-voters-view/', views.adminVotedVotersView, name='adminVotedVotersView'),
]