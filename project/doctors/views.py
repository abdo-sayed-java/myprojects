from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment

@login_required
def doctor_dashboard(request):
    doctor = request.user.doctor  # assuming OneToOneField from user to doctor

    # جميع المواعيد المرتبطة بهذا الدكتور
    appointments = Appointment.objects.filter(doctor=doctor)

    # عدد المواعيد
    appointments_count = appointments.count()

    # عدد المرضى المختلفين
    patients_count = appointments.values('patient').distinct().count()

    context = {
        'appointments_count': appointments_count,
        'patients_count': patients_count,
        'appointments': appointments.order_by('-date', '-time')[:5],  # أحدث 5 مواعيد
    }
    return render(request, 'doctors/dashboard.html', context)
