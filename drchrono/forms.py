"""django forms"""
from django import forms
from material import *

class CheckIn(forms.Form):
    """check-in"""
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    date_of_birth = forms.DateField(label='Date of Birth', required=False)

    layout = Layout(Row('first_name', 'last_name'), 'date_of_birth')

class UpdateContactInfo(forms.Form):
    """patient can update their emergency contact"""
    phone_number = forms.CharField(label="Phone Number (Required)")
    email = forms.CharField(label="Email Address", required=False)
    emergency_contact_name = forms.CharField(label="Emergency Contact Name", required=False)
    emergency_contact_phone = forms.CharField(label="Emergency Contact Phone Number", required=False)
    emergency_contact_relation = forms.CharField(label="Relation to You", required=False)

    layout = Layout('phone_number', 'email',
                    Row('emergency_contact_name',
                        'emergency_contact_phone',
                        'emergency_contact_relation'))
