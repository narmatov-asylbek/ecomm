from django import forms


class ApplyCouponForm(forms.Form):
    coupon = forms.CharField(max_length=50, label='Купон')