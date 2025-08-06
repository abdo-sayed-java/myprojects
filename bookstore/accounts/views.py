from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, UserUpdateForm
from .models import UserProfile
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registered Successfully!')
            return redirect('core:home')
    else:
        form = UserRegistrationForm()

    return render(request, 'patients/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {user.username}')
                return redirect('core:home')
    else:
        form = UserLoginForm()
    return render(request, 'patients/login.html', {'form': form})

@login_required
def profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile is Updated!')
            return redirect('patients:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form= UserProfileForm(instance=profile)
    return render(request, 'patients/profile.html', {
        'user_form' : user_form,
        'profile_form' : profile_form
    })

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You Have Been Logged Out!')
    return redirect('core:home')

@login_required
def order_history(request):
    orders = request.user.orders.all().order_by('-create_at')
    return render(request, 'patients/order_history.html', {'orders': orders})