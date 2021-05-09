import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import Task, ToDoList, User,  Course
from model_bakery import baker

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

class ModelsTestField_Func(TestCase):
    #test the str field
    def test_course_task_str(self):
        c = Course.objects.create(name ="Computer Science")
        t = Task.objects.create(description_text ="Final Project")
        self.assertEqual(str(c), "Computer Science")
        self.assertEqual(str(t), "Final Project")
    
    #testing many to many relationships between course and tasks
    def courses_to_tasks(self):
        t_n = Task.objects.create(description_text ="Final Project")
        c_n = Course.objects.create(name="Computer Science")
        c_n1 = Course.objects.create(name ="Science")
        c_n.t_n_set.add(t_n)
        c_n1.t_n_set.add(t_n)
        self.assertEqual(t_n.courses.count(), 2)
    
    def tasks_to_courses(self):
        t_n = Task.objects.create(description_text ="Final Project")
        c_n = Course.objects.create(name="Computer Science")
        c_n1 = Course.objects.create(name ="Science")
        t_n.courses.set([c_n.pk,c_n1.pk])
        self.assertEqual(t_n.courses.count(), 2)

    #testing all the different fields for created tasks using model bakery
    def Test_tasks_field(self):
        task = baker.make(Task, description_text="presentation")
        self.assertEqual(str(task), "presentation")



class Test_URL(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

