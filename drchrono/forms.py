"""django forms"""
from django import forms

class CheckIn(forms.Form):
    """check-in"""
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
