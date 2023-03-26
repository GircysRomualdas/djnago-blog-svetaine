from django.test import TestCase

from personal.views import (
    home_screen_view,
)
from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
)

class MysiteTest(TestCase):

    # Home tests
    def test_home_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'personal/home.html')

    def test_home_contains(self):
        response = self.client.get('/')
        self.assertContains(response, "Lorem, ipsum dolor")

    # Register tests
    def test_register_code(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_template(self):
        response = self.client.get('/register/')
        self.assertTemplateUsed(response, 'account/register.html')

    def test_register_contains(self):
        response = self.client.get('/register/')
        self.assertContains(response, "Register an account")
    
    # Login tests
    def test_login_code(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_contains(self):
        response = self.client.get('/login/')
        self.assertContains(response, "Log in")

    # Must authenticate tests
    def test_must_authenticate_code(self):
        response = self.client.get('/must_authenticate/')
        self.assertEqual(response.status_code, 200)

    def test_must_authenticate_template(self):
        response = self.client.get('/must_authenticate/')
        self.assertTemplateUsed(response, 'account/must_authenticate.html')

    def test_must_authenticate_contains(self):
        response = self.client.get('/must_authenticate/')
        self.assertContains(response, "Must authenticate to view this page.")