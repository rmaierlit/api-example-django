"""this modules contains the views for this project"""

##from social_auth_drchrono.backends import get_user_details

from django.shortcuts import render
from django.http import HttpResponseRedirect

from drchrono.api_helper import ApiHelper
from drchrono.forms import CheckIn

def check_in(request):
    """check-in page for patients"""
    response = ApiHelper(request.user).get_user_info()
    context = response
    if request.method == 'POST':
        form = CheckIn(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            response = ApiHelper(request.user).find_patient(first_name, last_name)
            patient_id = response['id']
            return HttpResponseRedirect('/patient/{}/update/'.format(patient_id))
    else:
        form = CheckIn()

    context.update(form=form)
    return render(request, 'drchrono/check-in.html', context)

def update_patient_info(request, patient_id):
    """the patient can confirm their information here"""
    context = {'patient_id': patient_id}
    return render(request, 'drchrono/update-patient-info.html', context)

def patient_appointment(request, patient_id):
    """the patient can see their latest appointment and confirm they are waiting to be seen"""
    context = {'appointments': ApiHelper(request.user).get_appointments(patient_id)}
    return render(request, 'drchrono/patient-appointment.html', context)

def patient_arrived(request, appointment_id):
    """confirms that the patient has checked in"""
    response = ApiHelper(request.user).mark_arrived(appointment_id)
    context = {'appointment_id': appointment_id}
    return render(request, 'drchrono/patient-arrived.html', context)
