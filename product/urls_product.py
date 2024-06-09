from django.urls import path
from . import views

app_name='product'
urlpatterns =[
    path('home/', views.home_page, name='home'),
    path('form_book/', views.form_book, name='form_book'),
    path('book/<int:pk>/', views.book_page, name='book_page'),
    path('book/delete/<int:pk>', views.delete_book, name='delete'),
    
]