"""Helper class to update Django models in the database"""

from drchrono.models import Patient, Appointment

class ModelHelper:
    """Helper methods to update models"""
    def add_patient(self, patient_info):
        """adds a patient to the database if it doesn't already exist"""
        patient = Patient.objects.filter(patient_id=patient_info['id'])

        if not patient:
            #if this patient is not already in the database
            patient = Patient(
                patient_id=patient_info['id'],
                first_name=patient_info['first_name'],
                last_name=patient_info['last_name'],
                date_of_birth=patient_info['date_of_birth']
            )
            patient.save()


        