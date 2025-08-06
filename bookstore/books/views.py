from zoneinfo import available_timezones

from django.contrib.admin.templatetags.admin_list import paginator_number
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaultfilters import title

from .models import Book, Category
from .forms import BookSearchForm
from cart.forms import CartAddBookForm

# Create your views here.

def book_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)

    form = BookSearchForm(request.GET or None)
    if form.is_valid():
        query = form.cleaned_data.get('query')
        category_filter = form.cleaned_data.get('category')

        if query:
            books = books.filter(title__icontains=query)
        if category_filter:
            books = books.filter(category=category_filter)

    paginator = Paginator(books, 6)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'books/book_list.html', {
        'category':category,
        'categories':categories,
        'books': books,
        'form':form,
    })

def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    cart_book_form = CartAddBookForm()
    return render(request, 'books/book_detail.html', {
        'book':book,
        'cart_book_form':cart_book_form
    })