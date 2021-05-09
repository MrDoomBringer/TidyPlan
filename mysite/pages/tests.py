import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import Task, ToDoList, User,  Course
from model_bakery import baker

class QuestionModelTests(TestCase):
    #authentication testing
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

class ModelsTestField_Func(TestCase):
    #test the str field
    def test_course_task_str(self):
        c = Course.objects.create(name ="Computer Science")
        t = Task.objects.create(description_text ="Final Project")
        self.assertEqual(str(c), "Computer Science")
        self.assertEqual(str(t), "Final Project")
    
    #testing many to many relationships between course and tasks
    def test_coursesTotasks(self):
        tn = Task.objects.create(description_text ="Final Project")
        cn = Course.objects.create(name = 'Computer Science')
        cn1 = Course.objects.create(name = 'Science')
        tn.courses.set([cn.pk,cn1.pk])
        self.assertEqual(tn.courses.count(),2)
    
    

    #testing all the different fields for created tasks using model bakery
    def test_tasks_field(self):
        task = baker.make(Task, description_text="presentation")
        self.assertEqual(str(task), "presentation")


#testing the homepage URL
class Test_URL(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

