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
            'https://drchrono.com/api/patients_summary?first_name={}&last_name={}'.format(
                first_name, last_name
            ),
            headers=self.headers,
        )
        return response.json()['results'][0]

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
        response = requests.patch(
            'https://drchrono.com/api/appointments/{}'.format(
                appointment_id
            ), 
            data={'status': 'Arrived'},
            headers=self.headers,
        )

        print ('status: ', response.status_code, response.content)