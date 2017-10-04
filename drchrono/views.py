"""this modules contains the views for this project"""

##from social_auth_drchrono.backends import get_user_details

from django.shortcuts import render
from django.http import HttpResponseRedirect

from drchrono.api_helper import ApiHelper
from drchrono.model_helper import ModelHelper
from drchrono.forms import CheckIn, UpdateContactInfo
from drchrono.models import Patient, Appointment

helper = ModelHelper()

def check_in(request):
    """check-in page for patients"""
    response = ApiHelper(request.user).get_user_info()
    context = response
    message = ''
    if request.method == 'POST':
        form = CheckIn(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            response = ApiHelper(request.user).find_patient(first_name, last_name)
            if response is None:
                # if a matching user is not found
                message = 'no user found matching this information'
            else:
                print (response.keys())
                helper.add_patient(response)
                patient_id = response['id']
                return HttpResponseRedirect('/patient/{}/update/'.format(patient_id))
    else:
        form = CheckIn()

    context.update(form=form, message=message)
    return render(request, 'drchrono/check-in.html', context)

def update_patient_info(request, patient_id):
    """the patient can confirm their information here"""
    context = Patient.objects.filter(patient_id=patient_id).values().first()

    if request.method == "POST":
        form = UpdateContactInfo(request.POST)
        if form.is_valid():
            ApiHelper(request.user).update_contact_info(patient_id, form.cleaned_data)
            return HttpResponseRedirect('/patient/{}/today'.format(context['patient_id']))
    else:
        form = UpdateContactInfo(initial={
            'phone_number': context['phone_number'],
            'email': context['email'],
            'emergency_contact_name': context['emergency_contact_name'],
            'emergency_contact_phone': context['emergency_contact_phone'],
            'emergency_contact_relation': context['emergency_contact_relation'],
            }) #context contains the patient info

    print('patient is ', context )
    context.update(form=form)

    return render(request, 'drchrono/update-patient-info.html', context)

def patient_appointment(request, patient_id):
    """the patient can see their latest appointment and confirm they are waiting to be seen"""
    appointments = ApiHelper(request.user).get_appointments(patient_id)
    for appointment in appointments:
        helper.add_appointment(appointment)
    context = {'appointments': appointments}
    return render(request, 'drchrono/patient-appointment.html', context)

def patient_arrived(request, appointment_id):
    """confirms that the patient has checked in"""
    ApiHelper(request.user).mark_arrived(appointment_id)

    appointment = Appointment.objects.get(pk=appointment_id)
    helper.start_waiting(appointment)
    context = {'appointment_id': appointment_id, 'patient_id': appointment.patient.patient_id}
    return render(request, 'drchrono/patient-arrived.html', context)

def waiting(request):
    """lists currently waiting patients"""
    waitlist = Appointment.objects.exclude(time_arrived=None).filter(time_seen=None)
    all_patients_seen = Appointment.objects.exclude(time_seen=None)
    average_wait = reduce(
        # sum the time each patient had to wait
        lambda total, appointment: total + (appointment.time_seen - appointment.time_arrived).total_seconds(),
        all_patients_seen, 0) / len(all_patients_seen) # then divide by total number of patients for the average
    context = {'waitlist': waitlist, 'average_wait': average_wait}
    return render(request, 'drchrono/waiting.html', context)

def patient_seen(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    patient = appointment.patient

    helper.patient_seen(appointment)
    context = {
        'patient_name': patient.first_name + ' ' + patient.last_name,
        'time_spent_waiting': (appointment.time_seen - appointment.time_arrived).total_seconds()
    }
    print(context)
    return render(request, 'drchrono/seen.html', context)