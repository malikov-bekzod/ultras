from django.urls import path
from .views import ShopView
urlpatterns = [
    path("", ShopView.as_view(), name="shop"),
    # path("add-product/", CreateProduct.as_view(), name="add-product"),
]
