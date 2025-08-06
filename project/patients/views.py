from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment

@login_required
def patient_dashboard(request):
    patient = request.user

    # احجز المواعيد القادمة فقط (الي تاريخها أكبر من أو تساوي النهارده)
    from datetime import date
    upcoming_appointments = Appointment.objects.filter(patient=patient, date__gte=date.today()).order_by('date', 'time')

    context = {
        'appointments_count': upcoming_appointments.count(),
        'medical_records_count': 0,  # حطها صفر دلوقتي
        'upcoming_appointments': upcoming_appointments,
        'recent_visits': [],  # لسه هنضيفها لو حبيت بعدين
    }
    return render(request, 'patients/dashboard.html', context)
