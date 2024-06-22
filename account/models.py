from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.FileField('Photo', upload_to='img_user/')
    bio = models.TextField(max_length=300, verbose_name='Bio')
    birth_date = models.DateTimeField('Birth Date')
    
    
    def __str__(self):
        return f'{self.user.username}'    