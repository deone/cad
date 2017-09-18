# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from data.models import Organization, Agent
from views import create_activate_deactivate_organization, create_activate_deactivate_agent

import copy

class ViewTest(TestCase):
    def setUp(self):
        self.c = Client()

class CreateActDeacOrganization(ViewTest):
    def setUp(self, *args, **kwargs):
        super(CreateActDeacOrganization, self).setUp(*args, **kwargs)
        self.data = {'name': 'Silver Street'}

    def test_create_organization(self):
        data = copy.deepcopy(self.data)
        data.update({'action': 'create'})

        response = self.c.post('/cad/organization', data=data)

        org = Organization.objects.all()[0]
        self.assertEqual(org.name, 'Silver Street')
        self.assertTrue(org.is_active)
        self.assertEqual(response.data, {u'message': u'Success!'})

    def test_act_organization(self):
        org = Organization.objects.create(name='Silver Street', is_active=False)

        data = copy.deepcopy(self.data)
        data.update({'action': 'act'})

        response = self.c.post('/cad/organization', data=data)

        self.assertTrue(Organization.objects.get(name='Silver Street').is_active)
        self.assertEqual(response.data, {u'message': u'Success!'})

        org.delete()

    def test_deac_organization(self):
        org = Organization.objects.create(name='Silver Street')

        data = copy.deepcopy(self.data)
        data.update({'action': 'deac'})

        response = self.c.post('/cad/organization', data=data)

        self.assertFalse(Organization.objects.get(name='Silver Street').is_active)
        self.assertEqual(response.data, {u'message': u'Success!'})

        org.delete()

class CreateActDeacAgent(ViewTest):
    def setUp(self, *args, **kwargs):
        super(CreateActDeacAgent, self).setUp(*args, **kwargs)
        self.data = {'first_name': 'Dayo', 'last_name': 'Osikoya'}

    def test_create_agent(self):
        data = copy.deepcopy(self.data)
        data.update({'action': 'create'})

        response = self.c.post('/cad/agent', data=data)

        agent = Agent.objects.all()[0]
        self.assertEqual(agent.first_name, 'Dayo')
        self.assertEqual(agent.last_name, 'Osikoya')
        self.assertTrue(agent.is_active)
        self.assertEqual(response.data, {u'message': u'Success!'})

    def test_act_agent(self):
        agent = Agent.objects.create(first_name='Dayo', last_name='Osikoya', is_active=False)

        data = copy.deepcopy(self.data)
        data.update({'action': 'act'})

        response = self.c.post('/cad/agent', data=data)

        self.assertTrue(Agent.objects.get(first_name='Dayo').is_active)
        self.assertEqual(response.data, {u'message': u'Success!'})

        agent.delete()

    def test_deac_agent(self):
        agent = Agent.objects.create(first_name='Dayo', last_name='Osikoya')

        data = copy.deepcopy(self.data)
        data.update({'action': 'deac'})

        response = self.c.post('/cad/agent', data=data)

        self.assertFalse(Agent.objects.get(first_name='Dayo').is_active)
        self.assertEqual(response.data, {u'message': u'Success!'})

        agent.delete()