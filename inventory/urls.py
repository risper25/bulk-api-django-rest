
from django.urls import path
from .views import ProductListAPIView,BulkProductListAPIView


urlpatterns = [
    path("products/",ProductListAPIView.as_view(),name="products"),
     path("products-bulk/",BulkProductListAPIView.as_view(),name="products-bulk"),
]