from . import views
from django.urls import path


urlpatterns = [
    path('basket/<int:user_id>/', views.basket_view, name='basket'),
]
