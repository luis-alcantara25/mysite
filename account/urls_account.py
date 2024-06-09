from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logging/', views.logging, name='logging'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'), 
    ]
