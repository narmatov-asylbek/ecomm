from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import OrderList, OrderDetail, OrderItemList, CouponList, CouponDetail, OrderItemDetail
from .views import CategoryList, CategoryDetail, ProductList, ProductDetail
from .views import api_root

urlpatterns = format_suffix_patterns([
    path('', api_root, name='main'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('order-item/', OrderItemList.as_view(), name='order_item-list'),
    path('order-item/<int:pk>/detail', OrderItemDetail.as_view(), name='orderitem-detail'),
    path('coupons/<int:pk>/detail', CouponDetail.as_view(), name='coupon-detail'),
    path('coupons/', CouponList.as_view(), name='coupon-list'),
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/detail/', CategoryDetail.as_view(), name='category-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/detail/', ProductDetail.as_view(), name='product-detail'),
])