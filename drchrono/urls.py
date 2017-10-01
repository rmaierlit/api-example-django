"""urls and routing for this project"""
from django.conf.urls import include, url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='drchrono/index.html'), name='home'),

    url(r'^check-in/$', views.check_in, name="check_in"),

    url(
        r'^patient/(?P<patient_id>[0-9]+)/update/$',
        views.update_patient_info,
        name="update_patient"
    ),

    url(
        r'^patient/(?P<patient_id>[0-9]+)/appointment/$',
        views.patient_appointment,
        name="patient_appointment"
    ),

    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
