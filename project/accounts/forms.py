from django import forms
from accounts.models import CustomUser
from doctors.models import Doctor

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    specialization = forms.CharField(required=False, help_text="Only required for doctors.")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
            if user.role == 'doctor':
                specialization = self.cleaned_data.get('specialization', 'Not specified')
                Doctor.objects.create(user=user, specialization=specialization)

        return user
