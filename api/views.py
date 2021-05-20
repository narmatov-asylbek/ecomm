from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from orders.models import Order, OrderItem
from coupons.models import Coupon
from shop.models import Category, Product
from .serializers import (
    OrderSerializer,
    OrderItemSerializer,
    CouponSerializer,
    CategorySerializer,
    ProductSerializer
)


@api_view(['GET'])
def api_root(request):
    return Response({
        'orders': reverse('order-list', request=request),
        'order_items': reverse('order_item-list', request=request),
        'coupons': reverse('coupon-list', request=request),
        'products': reverse('product-list', request=request),
        'category': reverse('category-list', request=request)
    })


# Orders
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Order Items
class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


# Coupons
class CouponList(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon
    serializer_class = CouponSerializer


# Products
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Category
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
