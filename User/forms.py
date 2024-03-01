from django import forms
from User.models import Registration, NextOfKin


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'phone_number', 'password']


class NextOfKinForm(forms.ModelForm):
    class Meta:
        model = NextOfKin
        fields = ['full_name', 'employee_name', 'ID_number', 'phone_number']
