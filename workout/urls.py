from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'workout'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('workout:login')), name='logout'),
    
    path('', views.run_list, name='run_list'),
    path('run/<str:pk>/', views.run_details, name='run_details'),
    path('add_new_run/', views.add_run, name='add_run'),
    path('run/<str:pk>/delete/', views.delete_run, name='delete_run'),
    path('run/<str:pk>/edit/', views.edit_run, name='edit_run'),
    path('date/<int:year>/', views.run_list, name='run_list_by_year'),
    path('date/<int:year>/<int:month>', views.run_list, name='run_list_by_year_month'),
]