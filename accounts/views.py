from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import survote_user
from .forms import survote_user_form
from voting.models import Voter

def login_page(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse('adminDashboard'))
        else:
            return redirect(reverse('voting:vote'))

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f'{user} logged in')
            if request.user.user_type == '1':
                # return redirect(reverse('adminDashboard'))
                return redirect(reverse('administrators:admin_dashboard'))
            else:
                return redirect(reverse('voting:vote'))
            
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/')
        
    context = {}
    return render(request, 'login.html', context)


def sign_up_page(request):
    userform = survote_user_form()
    message = ''

    if request.method == "POST":
        userform = survote_user_form(request.POST)

        if userform.is_valid():
            user = userform.save(commit=False)
            voter = Voter()
            voter.user = user 
            user.save()
            voter.save()

            messages.success(request, 'Account creation successful. You can now login')
            return redirect(reverse('accounts:login'))
        else:
            for error_type, error_message in userform.errors.items():
                for message in error_message:
                    messages.error(request, message)
            return redirect("accounts:sign_up")
        
    context = {'userform': userform}
    return render(request, 'sign_up.html', context)


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect(reverse('accounts:login'))
