from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from .models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormBook
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home_page(request):
    books = Book.objects.filter(rating__lte = 5)
    return render(request, 'product/home.html', {'books':books})
        
    
#Form for books
def form_book(request):
    if request.method =='GET':
        form = FormBook()
        return render(request, 'product/form_book.html', {'form':form})
    else:
        form = FormBook(request.POST)
        if form.is_valid:
            fm = form.save(commit=False)
            fm.author = request.user
            fm.save()
            messages.success(request, 'Your book has been saved susscessfully')
            return redirect('product:home')
        else:
            messages.error(request, 'The data for this book is invalid')
            return redirect('product:form_book')