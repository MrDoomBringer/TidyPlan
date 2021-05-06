import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import Task, ToDoList, User

class QuestionModelTests(TestCase):
    def test_no_questions(self):
        c = Client()
        user = User.objects.create_user("test_user", password="test_password")
        user.save()
        c.login(username="test_user", password="test_password")

        response = c.get(reverse('calendar'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks are available to view")
        self.assertQuerysetEqual(
            response.context['tsk_list'], 
            [])
