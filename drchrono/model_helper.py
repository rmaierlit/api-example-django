"""Helper class to update Django models in the database"""

from drchrono.models import Patient, Appointment

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


        