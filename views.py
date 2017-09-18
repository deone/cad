# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from data.models import Organization, Agent

def create_activate_deactivate_object(model_class, action, **kwargs):
    if action == 'create':
        model_class.objects.create(**kwargs)
    else:
        obj = model_class.objects.get(**kwargs)
        if action == 'deac':
            if obj.is_active:
                obj.is_active = False
        elif action == 'act':
            if not obj.is_active:
                obj.is_active = True
        obj.save()

    return Response({'message': 'Success!'})

@api_view(['POST'])
def create_activate_deactivate_organization(request):
    action = request.data['action']
    name = request.data['name']
    data = {'name': name}

    return create_activate_deactivate_object(Organization, action, **data)

@api_view(['POST'])
def create_activate_deactivate_agent(request):
    action = request.data['action']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    data = {'first_name': first_name, 'last_name': last_name}

    return create_activate_deactivate_object(Agent, action, **data)