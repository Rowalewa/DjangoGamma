from django.contrib import messages
from django.shortcuts import render, redirect

from User.forms import RegistrationForm, NextOfKinForm


# Create your views here.


def employee_registration(request):
    form = RegistrationForm()
    if request.method == 'GET':  # takes the records and populates on url, how url chrome behaves
        form = RegistrationForm()
        return render(request, 'Employee_registration.html', {'form': form})
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Employee')
            return redirect('employee_registration')


def employee_next_of_kin(request):
    form = NextOfKinForm()
    if request.method == 'GET':  # takes the records and populates on url, how url chrome behaves
        form = NextOfKinForm()
        return render(request, 'EmployeeNextOfKinDetails.html', {'form': form})
    else:
        form = NextOfKinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Next of Kin')
            return redirect('employee_next_of_kin')

