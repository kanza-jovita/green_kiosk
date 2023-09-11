from django.urls import path
from .views import upload_product
from .import views
from .views import product_detail
from .views import products_list
from .views import edit_product
urlpatterns = [
    path("products/upload", upload_product, name="product_upload_view"),
    path("products/list", products_list, name = "products_list_view"),
    path("products/<int:id>/",product_detail, name="product_detail_view"),
    path("products/edit/<int:id>",edit_product, name = "product_edit_view"),
    path('search/', views.search_results, name='search_results'),
    

]
