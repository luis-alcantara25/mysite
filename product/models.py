from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    class TypeChoices(models.TextChoices):
            ACCION = 'ACN', 'Accion'
            ADVENTURE = 'ATR', 'Adventure'
            COMEDY = 'CMD', 'Comedy'
            ROMANCE = 'RMC', 'Romance'
            CRIME = 'CRM', 'Crime'
            ANIMATION = 'ANMT', 'Animation'
            
    img_book = models.ImageField('Image',upload_to='img_books/', default='img_books/hero-inferior.svg')
    title = models.CharField('Title', max_length=100, unique=True)
    tagline = models.CharField('Tagline', max_length=300)
    gender = models.CharField(max_length=4, choices=TypeChoices, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    
    def __str__(self):
        return f'{self.title}'
    
    def my_img_book(self):
        if self.img_book:
            return self.img_book.url
        else:
            return '/img_books/hero-inferior.svg'    
        
# Products

class Car(models.Model):
    product = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)