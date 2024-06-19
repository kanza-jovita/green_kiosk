from django.urls import path
from .views import CustomerListView
from .views import AddToCartView

urlpatterns = [
    path("customers/", CustomerListView.as_view(),name = "customer_list_view"),
    path("customers/<int:id>/",CustomerListView.as_view(),name = "customer_detail_view"),
    path("add_to_cart/", AddToCartView.as_view(), name="add_to_cart_view"),
]