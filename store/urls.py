from django.urls import path
from . import views as store_views

urlpatterns = [
    path('', store_views.home, name='home'),
    path('<int:product_id>/view', store_views.view, name='product_detail'),
    path('create/', store_views.create_product, name='create'),
    path('<int:product_id>/update', store_views.update_product, name='update'),
    path('<int:product_id>/delete', store_views.delete_product, name='delete'),
]
