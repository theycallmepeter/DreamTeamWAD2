from django.test import TestCase,Client
from gliocas_app.models import Course,Subject, Followed,Question, UpvoteQuestion,UpvoteAnswer
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404
import datetime

# Create your tests here.


class FollowTests(TestCase):

    def test_can_follow_courses(self):

        #create course
        subject = Subject.objects.create(name='abcd')
        subject.save()

        course= Course.objects.create(name='ab',subject = subject)
        course.save()

        #create user
        user = User.objects.create(username='test')
        user.set_password('12345')
        user.save()

        c = Client()
        c.login(username='test',password='12345')

        response = c.get(reverse('follow',kwargs={'course_slug':'ab','subject_slug':'abcd'}))

        exists = False
        try:
            get_object_or_404(Followed,poster=user,course=course)
            exists=True
        except:
            exists=False

        self.assertTrue(exists)


    #can follow courses only when logged in
    def test_can_follow_courses_only_when_logged_in(self):

        #create course
        subject = Subject.objects.create(name='abcd')
        subject.save()

        course= Course.objects.create(name='ab',subject = subject)
        course.save()

        c = Client()

        response = c.get(reverse('follow',kwargs={'course_slug':'ab','subject_slug':'abcd'}))

        exists = False

        try:
            get_object_or_404(Followed,poster=user,course=course)
            exists=True
        except:
            exists=False

        self.assertFalse(exists)
#test login
class loginTests(TestCase):

    #cant register if logged in
    def test_cant_register_if_logged_in(self):
        user = User.objects.create(username='test')
        user.set_password('12345')
        user.save()

        c= Client()

        c.login(username='test',password='12345')

        response = c.get(reverse('register'))

        self.assertNotContains(response,'<form')

    #have to logout before loging in from different account
    def test_cant_login_when_logged_in(self):
        user = User.objects.create(username='test')
        user.set_password('12345')
        user.save()

        c= Client()

        c.login(username='test',password='12345')

        response = c.get(reverse('login'))

        self.assertNotContains(response,'<form')


#test courses
class courseTests(TestCase):

    #can only like a question once
    def test_can_like_only_once(self):
        subject = Subject.objects.create(name='abcd')
        subject.save()
        course= Course.objects.create(name='ab',subject = subject)
        course.save()
        user = User.objects.create(username='test')
        user.set_password('12345')
        user.save()

        question = Question.objects.create(poster=user,course=course)
        question.text='abcd'
        question.title='abcd'
        question.date = datetime.datetime.now()
        question.save()


        c=Client()
        c.login(username='test',password='12345')

        c.get(reverse('like_question',kwargs={'subject_slug':subject.slug,
                                        'course_slug':course.slug,
                                        'question_slug':question.slug,
                                        'like':'1'}))
        c.get(reverse('like_question',kwargs={'subject_slug':subject.slug,
                                        'course_slug':course.slug,
                                        'question_slug':question.slug,
                                        'like':'1'}))
        c.get(reverse('like_question',kwargs={'subject_slug':subject.slug,
                                        'course_slug':course.slug,
                                        'question_slug':question.slug,
                                        'like':'1'}))
        self.assertEqual(len(UpvoteQuestion.objects.filter(user=user)),1)

        #can Dislike only once
    def test_can_dislike_only_once(self):
        subject = Subject.objects.create(name='abcd')
        subject.save()
        course= Course.objects.create(name='ab',subject = subject)
        course.save()
        user = User.objects.create(username='test')
        user.set_password('12345')
        user.save()

        question = Question.objects.create(poster=user,course=course)
        question.text='abcd'
        question.title='abcd'
        question.date = datetime.datetime.now()
        question.save()


        c=Client()
        c.login(username='test',password='12345')

        c.get(reverse('like_question',kwargs={'subject_slug':subject.slug,
                                        'course_slug':course.slug,
                                        'question_slug':question.slug,
                                        'like':'0'}))
        c.get(reverse('like_question',kwargs={'subject_slug':subject.slug,
                                        'course_slug':course.slug,
                                        'question_slug':question.slug,
                                        'like':'0'}))
        c.get(reverse('like_question',kwargs={'subject_slug':subject.slug,
                                        'course_slug':course.slug,
                                        'question_slug':question.slug,
                                        'like':'0'}))
        self.assertEqual(len(UpvoteQuestion.objects.filter(user=user)),1)
