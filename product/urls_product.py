from django.urls import path
from . import views

app_name='product'
urlpatterns =[
    path('home/', views.home_page, name='home'),
    path('form_book/', views.form_book, name='form_book')
]