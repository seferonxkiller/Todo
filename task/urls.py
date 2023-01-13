from django.urls import path
from .views import index, edit, create, delete, login_view, logout_view, register_view

app_name = 'task'

urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register')
]
