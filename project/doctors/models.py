from django.db import models
from django.conf import settings

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctor_photos/', blank=True, null=True)  # حقل الصورة

    def __str__(self):
        return self.user.get_full_name()
