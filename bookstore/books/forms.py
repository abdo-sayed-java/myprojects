from django import forms
from .models import Book,Category

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All Categories"
    )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['category', 'title', 'author', 'description', 'price', 'cover_image', 'available']