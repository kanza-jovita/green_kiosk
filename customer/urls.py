
from .views import customer_list,customer_detail,customer_edit, upload_customer
from django.urls import path
urlpatterns =[
    path("customer/upload", upload_customer, name="upload_customer_view"),
    path("customer/list",  customer_list, name="customer_list_view"),
    path("customer/<int:id>/",  customer_detail, name="customer_detail_view"),
    path("customer/edit/<int:id>/",customer_edit,name="customer_edit_view" )
]

