from django.test import TestCase
from accounts.forms import RegistrationForm, EditProfileForm, ProjectCreateForm, EditProjectForm
import tempfile


class TestForms(TestCase):
    def test_registration(self):
        #form_data = {'first_name': 'First', 'last_name': 'Last', 'email': 'Email@innopolis.ru'}
        form_data = {'username': 'username', 'first_name': 'username', 'last_name': 'username',
                     'email': 'username@innopolis.ru', 'password1': '123qwe[]', 'password2': '123qwe[]'}

        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_editprofile(self):
        #form_data = {'first_name': 'First', 'last_name': 'Last', 'email': 'Email'}
        form_data = {'first_name': 'First', 'last_name': 'Last', 'email': 'Email@innopolis.ru'}

        form = EditProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_project(self):
        form_data = {'title': 'Title', 'type': 'Type', 'description': 'description'}
        #form_data = {'type': 'Type', 'description': 'description'}
        form = ProjectCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_edit_project(self):
        form_data = {'title': 'Title', 'type': 'Type', 'description': 'description'}
        #form_data = {'type': 'Type', 'description': 'description'}
        form = EditProjectForm(data=form_data)
        self.assertTrue(form.is_valid())