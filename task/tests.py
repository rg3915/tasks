from django.test import TestCase
from django.db.utils import IntegrityError
from task.models import Task
from django.test import Client
from django.contrib.auth.models import User


class CreateTaskTestCase(TestCase):

    def test_create_task_empty(self):
        self.assertIsNotNone(Task.objects.create())

    def test_create_task_without_name(self):
        with self.assertRaises(IntegrityError):
            Task.objects.create(name=None)

    def test_create_task_with_name(self):
        self.assertIsNotNone(Task.objects.create(name='tarefa'))


class HomeTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='admin', password='admin')

    def test_home_access(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Olá')

    def test_home_link_login(self):
        response = self.client.get('/')
        self.assertContains(response, 'Login')
        self.client.login(username='admin', password='admin')
        response = self.client.get('/')
        self.assertNotContains(response, 'Login')

    def test_login_back_to_home(self):
        response = self.client.get('/')
        if not response.context['user'].is_authenticated():
            self.assertContains(
                response, '<a href="/admin/login/?next=/"><button type="button" class="btn btn-primary">Login</button></a>', html=True)
