from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import Coupon
from .forms import ApplyCouponForm


@require_POST
def apply_coupon(request):
    now = timezone.now()
    coupon_form = ApplyCouponForm(request.POST)
    if coupon_form.is_valid():
        try:
            code = coupon_form.cleaned_data.get('coupon')
            coupon = Coupon.objects.get(code__iexact=code, valid_to__gte=now, valid_from__lte=now)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None

    return redirect('cart:cart_detail')

