from django.test import TestCase,Client
from gliocas_app.models import Course,Subject, Followed,Question, UpvoteQuestion,UpvoteAnswer,Reply, Answer
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils import timezone
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from gliocas_app.forms import UserForm
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
    def test_can_follow_only_once(self):
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
        response = c.get(reverse('follow',kwargs={'course_slug':'ab','subject_slug':'abcd'}))
        response = c.get(reverse('follow',kwargs={'course_slug':'ab','subject_slug':'abcd'}))

        self.assertEqual(len(Followed.objects.filter(poster=user,course=course)),1)
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

    def test_duplicate_usernames(self):
        #register user
        data={'username':'abcd','email':'test@test.com','password':'12345','confirm_password':'12345'}
        c = Client()
        c.post(reverse('register'),{'username':'abcd','email':'test@test.com','password':'12345','confirm_password':'12345'})

        #register user with same name
        data={'username':'abcd','email':'test1@test.com','password':'123456','confirm_password':'123456'}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())

    def test_not_matching_passwords_on_registration(self):
        data={'username':'abcd','email':'test@test.com','password':'12345','confirm_password':'123456'}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())




#test courses
class questionTests(TestCase):

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
        question.date = timezone.now()
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
        question.date = timezone.now()
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

    def test_image_displayed_in_qestion(self):
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
        question.date = timezone.now()
        question.picture = SimpleUploadedFile(name='test_image.jpg', content=open('gliocas_app/testimage/test.jpeg', 'rb').read(), content_type='image/jpeg')
        question.save()

        c=Client()

        response=c.get(reverse('show_question',kwargs={'course_slug':course.slug,'subject_slug':subject.slug,'question_slug':question.slug}))

        self.assertContains(response,'<img')

    def test_can_answer_only_when_logged_in(self):
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
        question.date = timezone.now()
        question.save()

        c = Client()

        response=c.get(reverse('answer_question',kwargs={'course_slug':course.slug,'subject_slug':subject.slug,'question_slug':question.slug}))

        self.assertEqual(response.status_code,302)

    def test_can_reply_to_answer_only_when_logged_in(self):
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
        question.date = timezone.now()
        question.save()

        answer = Answer.objects.create(poster=user,text='abcdef',question=question)

        c = Client()

        response=c.get(reverse('reply_answer',kwargs={'course_slug':course.slug,'subject_slug':subject.slug,'question_slug':question.slug,'answer_key':answer.pk}))

        self.assertEqual(response.status_code,302)

class addingTests(TestCase):

    def test_cant_add_subject_when_not_superuser(self):
        user = User.objects.create(username='test')
        user.set_password('12345')
        user.save()

        c= Client()
        c.login(username='test',password='12345')

        response = c.get(reverse('add_subject'))
        self.assertNotContains(response,'<form')

    def test_cant_add_course_when_not_superuser(self):
        user = User.objects.create(username='test')
        user.set_password('12345')
        user.save()

        subject = Subject.objects.create(name='abcd')
        subject.save()

        c= Client()
        c.login(username='test',password='12345')
        response = c.get(reverse('add_course',kwargs={'subject_slug':subject.slug}))
        self.assertEqual(response.status_code,302)
