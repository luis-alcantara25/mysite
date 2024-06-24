from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from product.models import Book
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from .models import Profile


# Views Creations

#SignUp User
def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html', {'forms':UserForm})
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if request.POST['password1'] == request.POST['password2']:
                if form.is_valid:
                    form.save()
                    messages.success(request, f'Tu cuenta ya fue creada, puedes iniciar session.')
                    return redirect('account:logging')
                else:
                    print(request.POST)
                    messages.error(request, 'Your data is invalid')
                    return render(request, 'account/signup.html', {'forms':UserForm})
            else:
                messages.error(request, "The passwords dind't match")
                return render(request, 'account/signup.html', {'forms':UserForm})
            
#Logging page
def logging(request):
    if request.user.is_authenticated:
        return redirect('product:home')
    else:
        if request.method == 'GET':
            return render(request, 'account/logging.html', {'log':AuthenticationForm})
        else:
            if request.method == 'POST':
                form = AuthenticationForm(request.POST)
                if form.is_valid:
                    username = request.POST['username']
                    password = request.POST['password']
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, f'Bienvenido {username}')
                        return redirect('product:home')
                    else:
                        messages.error(request, 'The Username or Password is incorrect')
                        return render(request, 'account/logging.html', {'log':AuthenticationForm})
                else:
                    messages.error(request, 'The data is invalid')
                    return render(request, 'account/logging.html', {'log':AuthenticationForm})
            else:
                return render(request, 'account/logging.html', {'log':AuthenticationForm})
                
            
#LogOut the User
@login_required
def logout_user(request):
    logout(request)
    return redirect('account:logging')


#user-profile
def email_check(user):
    return user.email.endswith('@gmail.com')

@login_required
@user_passes_test(email_check)
def profile(request):
    if request.user.has_perm('product.view_book'):
        book = Book.objects.filter(author=request.user)
        profile = Profile.objects.filter(user=request.user)
        return render(request, 'account/profile.html', {'books':book, 'users':profile})
    else:
        return HttpResponse('The User has not perm')