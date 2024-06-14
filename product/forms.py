from django.forms import ModelForm
from .models import Book

class FormBook(ModelForm):
    class Meta:
        model = Book
        fields = ['img_book', 'title', 'tagline', 'gender', 'rating']