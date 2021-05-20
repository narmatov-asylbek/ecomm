from django.shortcuts import render
from .tasks import order_created

from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm

# Create your views here.


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST or None)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clear()
            order_created.delay(order.id)
            return render(request, 'orders/created.html', {'order':order})
    else:
        order_form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'order_form': order_form})
