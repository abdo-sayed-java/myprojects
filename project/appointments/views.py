from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('patient_dashboard')  # بعد الحجز يرجعه للداشبورد
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

    if request.method == 'POST':
        appointment.delete()
        return redirect('patient_dashboard')

    # لو حابب تعمل صفحة تأكيد لاحقًا، ممكن تعملها
    return redirect('patient_dashboard')