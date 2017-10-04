"""Helper class for DrCrhono API"""
import datetime
import requests

class ApiHelper:
    """Helper methods for DrChrono API"""
    def __init__(self, user):
        access_token = user.social_auth.get(user=user).extra_data['access_token']
        self.headers = {'Authorization': 'Bearer {0}'.format(access_token)}

    def get_user_info(self):
        """retrieves user info from drchrono API"""
        response = requests.get('https://drchrono.com/api/users/current', headers=self.headers)
        return response.json()

    def find_patient(self, first_name, last_name):
        """searchs api for matching patient"""
        response = requests.get(
            'https://drchrono.com/api/patients?first_name={}&last_name={}'.format(
                first_name, last_name
            ),
            headers=self.headers,
        )

        response = response.json()

        if response.has_key('results') and response['results']:
            return response['results'][0]
        #else if no matching patient found
        return None

    def get_appointments(self, patient_id):
        """retrieves all appointments for the current day"""
        today = datetime.date.today()
        response = requests.get(
            'https://drchrono.com/api/appointments?patient={}&date={}'.format(
                patient_id, str(today)
            ),
            headers=self.headers,
        )
        return response.json()['results']

    def mark_arrived(self, appointment_id):
        """changes the status of an appointment to 'Arrived' """
        requests.patch(
            'https://drchrono.com/api/appointments/{}'.format(
                appointment_id
            ),
            data={'status': 'Arrived'},
            headers=self.headers,
        )

    def update_contact_info(self, patient_id, contact_info):
        """updates the patients cell phone, email, and emergency contact info"""
        requests.patch(
            'https://drchrono.com/api/patients/{}'.format(
                patient_id
            ),
            data={
                'cell_phone': contact_info['phone_number'],
                'email': contact_info['email'],
                'emergency_contact_name': contact_info['emergency_contact_name'],
                'emergency_contact_phone': contact_info['emergency_contact_phone'],
                'emergency_contact_relation': contact_info['emergency_contact_relation'],
            },
            headers=self.headers,
        )