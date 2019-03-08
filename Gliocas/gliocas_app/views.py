from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import RedirectView
from gliocas_app.forms import QuestionForm
from gliocas_app.models import Subject, Course, Question

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

# @login_required
def add_question(request, subject_slug, course_slug):
    
    form = QuestionForm()
    try:
        course = Course.objects.get(slug=course_slug)
        #TODO implement with user = request.user.pk after auth is finished
        user = User.objects.get_or_create(username = 'peter')[0].pk
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
                question.slug = slugify(question.pk) 
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
    context_dict = {}
    return render(request,'gliocas_app/register.html', context = context_dict)
    
def user_login(request):
    context_dict = {}
    return render(request,'gliocas_app/login.html', context = context_dict)


class PostLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug = slug)
        question_url = question.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            like_question(self.request, question)
        return obj_url

@login_required
def like_question(request, question, ):
    question_id = None
    if request.method == 'GET':
        question_id = request.GET['question_id']
    likes = 0
    if question_id:
        question = question.objects.get(id=int(question_id))
        if question:
            likes = question.likes + 1
            question.likes = likes
            question.save()
    return HttpResponse(likes)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
