from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from books.models import Book
from .models import Cart, CartItem, Order, OrderItem
from .forms import CartAddBookForm, CheckoutForm


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@login_required
@require_POST
def cart_add(request, book_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)

    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={'quantity': quantity, 'price': book.price}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        messages.success(request, f"{book.title} added to your cart.")

    return redirect('cart:cart_detail')


@login_required
@require_POST
def cart_remove(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from your cart.")
    return redirect('cart:cart_detail')


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)

    if not cart.items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('books:book_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create order
            order = Order.objects.create(
                user=request.user,
                total_price=cart.total_price,
                shipping_address=form.cleaned_data['shipping_address'],
                payment_method=form.cleaned_data['payment_method']
            )

            # Create order items
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    book=item.book,
                    quantity=item.quantity,
                    price=item.price
                )

            cart.items.all().delete()

            messages.success(request, "Your order has been placed successfully!")
            return redirect('patients:order_history')
    else:
        form = CheckoutForm(initial={
            'shipping_address': request.user.address
        })

    return render(request, 'cart/checkout.html', {
        'cart': cart,
        'form': form
    })