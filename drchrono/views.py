"""this modules contains the views for this project"""

##from social_auth_drchrono.backends import get_user_details

import requests

from django.shortcuts import render

from api_helper import ApiHelper

def check_in(request):
    """check-in page for patients"""
    response = ApiHelper(request.user).get_user_info()
    context = response.json()
    return render(request, 'drchrono/check-in.html', context)
