import requests

class ApiHelper:
    def __init__(self, user):
        access_token = user.social_auth.get(user=user).extra_data['access_token']
        self.headers = {'Authorization': 'Bearer {0}'.format(access_token)}

    def get_user_info(self):
        '''retrieves user info from drchrono API'''
        response = requests.get('https://drchrono.com/api/users/current', headers=self.headers)
        return response