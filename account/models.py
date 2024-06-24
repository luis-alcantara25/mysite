from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField('Photo', upload_to='img_user/', default='img_user/desarrollador-ejemplo.svg')
    bio = models.TextField(max_length=300, verbose_name='Bio', null=True, blank=True)
    birth_date = models.DateField('Birth Date', default='')
    

    def __str__(self):
        return f'{self.user.username}'
    
    def img_profile(self):
        if self.photo:
            return self.photo.url
        else:
            return 'img_user/desarrollador-ejemplo.svg'