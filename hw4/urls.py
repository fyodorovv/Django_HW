from . import views
from django.urls import path


urlpatterns = [
    path('prod_edit', views.edit_product_view, name='prod_edit'),
    path('add_image', views.add_image_view, name='add_image'),
]
