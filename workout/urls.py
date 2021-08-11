from django.urls import path
from . import views

app_name = 'workout'

urlpatterns = [
    path('', views.run_list, name='run_list'),
    path('run/<str:pk>/', views.run_details, name='run_details'),
    path('add_new_run/', views.add_run, name='add_run'),
    path('run/<str:pk>/delete/', views.delete_run, name='delete_run'),
    path('run/<str:pk>/edit/', views.edit_run, name='edit_run'),
    path('date/<int:year>/', views.run_list, name='run_list_by_year'),
    path('date/<int:year>/<int:month>', views.run_list, name='run_list_by_year_month'),
]