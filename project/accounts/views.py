from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from doctors.models import Doctor
from django.db import IntegrityError
from django.contrib import messages


# Create your views here.

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'accounts/home.html', {'doctors': doctors})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data.get('role')
            specialization = form.cleaned_data.get('specialization')

            user.save()  # احفظ اليوزر أولًا

            if role == 'doctor':
                try:
                    Doctor.objects.create(user=user, specialization=specialization)
                except IntegrityError:
                    messages.error(request, "This doctor already exists.")
                    return redirect('register')

            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})