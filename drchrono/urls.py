"""urls and routing for this project"""
from django.conf.urls import include, url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'check-in', views.check_in, name="check_in"),

    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
