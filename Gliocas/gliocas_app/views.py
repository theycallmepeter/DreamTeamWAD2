from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from gliocas_app.forms import QuestionForm
from gliocas_app.forms import UserForm
from django.contrib.auth.models import User
from gliocas_app.models import Subject, Course, Question, UpvoteQuestion, UpvoteAnswer, UpvoteReply


def index(request):
    context_dict = {}
    subject_list = Subject.objects.all()
    context_dict['subjects'] = subject_list
    return render(request, 'gliocas_app/index.html', context = context_dict)

def about(request):
    context_dict = {}
    return render(request, 'gliocas_app/about.html', context = context_dict)

def contact(request):
    context_dict = {}
    return render(request,'gliocas_app/contact.html',context = context_dict)

def subjects(request):
    context_dict = {}
    context_dict['subjects'] = Subject.objects.all();
    return render(request,'gliocas_app/subjects.html',context = context_dict)

def show_subject(request, subject_slug):
    context_dict = {}
    try:
        subject = Subject.objects.get(slug=subject_slug)
        courses = Course.objects.filter(subject=subject)
        context_dict['courses'] = courses
        context_dict['subject'] = subject
    except Subject.DoesNotExist:
        context_dict['courses'] = None
        context_dict['subject'] = None
    return render(request, 'gliocas_app/subject.html', context = context_dict)

def show_course(request, subject_slug, course_slug):
    context_dict = {}
    try:
        parent_subject = Subject.objects.get(slug=subject_slug)
        course = Course.objects.get(slug=course_slug)
        questions = Question.objects.filter(course=course)
        context_dict['questions'] = questions
        context_dict['course'] = course
        context_dict['subject'] = parent_subject
    except Subject.DoesNotExist:
        context_dict['subject'] = None
        context_dict['questions'] = None
        context_dict['course'] = None
    return render(request, 'gliocas_app/course.html', context = context_dict)

def show_question(request, subject_slug, course_slug, question_slug):
    context_dict = {}
    try:
        question = Question.objects.get(slug=question_slug)
        parent_course = Course.objects.get(slug=course_slug)
        parent_subject = Subject.objects.get(slug=subject_slug)
        context_dict['question'] = question
        context_dict['subject'] = parent_subject
        context_dict['course'] = parent_course
    except Question.DoesNotExist:
        context_dict['question'] = None
        context_dict['subject'] = None
        context_dict['course'] = None

    return render(request,'gliocas_app/question.html', context = context_dict)

@login_required
def add_question(request, subject_slug, course_slug):
    
    form = QuestionForm()
    try:
        course = Course.objects.get(slug=course_slug)
        #TODO implement with user = request.user.pk after auth is finished
        user = request.user.pk
    except Course.DoesNotExist:
        course = None
        user = None
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            if course and user:
                question = form.save(commit=False)
                question.course = course
                question.poster_id = user
                question.views = 0
                question.save()
                #2nd save so we have a unique slug from pk, will fix later
                question.save()
                return show_course(request, subject_slug, course_slug)
        else:
            print(form.errors)

    context_dict = {}
    context_dict['form'] = form
    context_dict['subject'] = Subject.objects.get(slug=subject_slug)
    context_dict['course'] = Course.objects.get(slug=course_slug)
    context_dict['course_slug'] = course_slug.lower()
    context_dict['subject_slug'] = subject_slug.lower()
    return render(request,'gliocas_app/add_question.html', context = context_dict)

def register(request):
    registered = False

    if request.method == 'POST':

        #get data from forms
        user_form = UserForm(data=request.POST)

        #check if forms are valid
        if user_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            login(request,user)

        else:
            print(user_form.errors)
    else:
        user_form= UserForm()


    return render(request,'gliocas_app/register.html',
                        {'user_form':user_form,
                        'registered':registered})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:

                return HttpResponse("Your Gliocas account is disabled.")
        else:

            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'gliocas_app/login.html', {})


# class PostLikeRedirect(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         slug = self.kwargs.get("slug")
#         question = get_object_or_404(Question, slug = slug)
#         question_url = question.get_absolute_url()
#         user = self.request.user
#         if user.is_authenticated():
#             like_question(self.request, question)
#         return obj_url

@login_required
def like_question(request, subject_slug, course_slug, question_slug, like):
    question = get_object_or_404(Question, slug = question_slug)
    user = request.user
    if UpvoteQuestion.objects.filter(question=question, user=user).exists():
        UpvoteQuestion.objects.get(question=question, user=user).delete()
        print('deleted upvote')
    elif like == '1':
        upvote = UpvoteQuestion.objects.create(question=question, user=user)
        upvote.save()
        print('upvoted')
    else:
        upvote = UpvoteQuestion.objects.create(question=question, user=user, positive=False)
        upvote.save()
        print('downvoted')
    return show_question(request, subject_slug, course_slug, question)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
