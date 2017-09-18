from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^organization', views.create_activate_deactivate_organization),
    url(r'^agent', views.create_activate_deactivate_agent),
]