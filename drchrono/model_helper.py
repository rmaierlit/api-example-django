"""Helper class to update Django models in the database"""

from drchrono.models import Patient, Appointment

from django.utils import timezone

class ModelHelper:
    """Helper methods to update models"""
    def add_patient(self, patient_info):
        """adds a patient to the database (and overwrites if that patient exists)"""
        patient = Patient(
            patient_id=patient_info['id'],
            first_name=patient_info['first_name'],
            last_name=patient_info['last_name'],
            date_of_birth=patient_info['date_of_birth'],
            phone_number=patient_info['cell_phone'],
            email=patient_info['email'],
            emergency_contact_name=patient_info['emergency_contact_name'],
            emergency_contact_phone=patient_info['emergency_contact_phone'],
            emergency_contact_relation=patient_info['emergency_contact_relation'],
        )
        patient.save()

    def add_appointment(self, app):
        """adds appointment"""
        patient = Patient.objects.get(pk=app['patient'])
        appointment = Appointment(
            appointment_id= app['id'],
            patient = patient,
            scheduled_time = app['scheduled_time'],
            duration = app['duration'],
            status = app['status'],
        )
        appointment.save()

    def start_waiting(self, appointment):
        """sets status to Arrived and records time arrived"""
        appointment.status = "Arrived"
        appointment.time_arrived = timezone.now()
        appointment.save()

    def patient_seen(self, appointment):
        """sets status to In Room and records time patient was seen"""
        appointment.status = "In Room"
        appointment.time_seen = timezone.now()
        appointment.save()
        