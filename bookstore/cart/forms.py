from django import forms
from .models import CartItem


class CartAddBookForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, max_value=20, initial=1)

    class Meta:
        model = CartItem
        fields = ['quantity']


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(widget=forms.Textarea)
    payment_method = forms.ChoiceField(choices=[
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ])