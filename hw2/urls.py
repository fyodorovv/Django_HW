from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users_view, name='users'),
    path('items/', views.items_view, name='items'),
]
