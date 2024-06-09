from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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
        
#Update book
def book_page(request, pk):
    
    book = Book.objects.get(id=pk)#get the Book from the database with its id.
    if request.method == 'POST':
        form = FormBook(request.POST, instance=book)# to pre-populate the data with ths instance value
        if form.is_valid:
            form.save()
            return redirect('product:home')
        else:
            messages.error(request, 'The data is invalid')
            return render(request, 'product/book.html', {'books',form})
    else:
        form = FormBook(instance=book)
    return render(request, 'product/book.html', {'form':form, 'books':book})

#delete book

def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    book.delete()
    return redirect('product:home')