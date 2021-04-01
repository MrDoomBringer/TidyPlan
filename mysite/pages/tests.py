import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Task, ToDoList, User

class QuestionModelTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('calendar'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks are available to view")
        self.assertQuerysetEqual(
            response.context['tsk_list'], 
            [])
