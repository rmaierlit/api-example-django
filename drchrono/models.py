"""Data models stored by django local to this server (outside of DrChrono API)"""
from django.db import models

class Patient(models.Model):
    """Patient information needed for app"""
    patient_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()

class Appointment(models.Model):
    """Appointment information needed for app"""
    appointment_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    duration = models.IntegerField()
    status = models.CharField(max_length=100)
    time_arrived = models.DateTimeField("time when patient checked in", null=True)
    time_seen = models.DateTimeField("time when doctor saw patient", null=True)
