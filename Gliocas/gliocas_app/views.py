from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import RedirectView
from gliocas_app.forms import QuestionForm, CourseForm, SubjectForm, AnswerForm, ReplyForm
from gliocas_app.forms import UserForm
from django.contrib.auth.models import User
from gliocas_app.search import search_query
from gliocas_app.models import Subject, Course, Question, UpvoteQuestion, UpvoteAnswer, UpvoteReply, Subject, Answer, Reply



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
        answers = Answer.objects.filter(question=question)
        replies = []
        for answer in answers:
            replies += Reply.objects.filter(answer=answer)
        parent_course = Course.objects.get(slug=course_slug)
        parent_subject = Subject.objects.get(slug=subject_slug)
        context_dict['question'] = question
        context_dict['answers'] = answers
        context_dict['replies'] = replies
        context_dict['subject'] = parent_subject
        context_dict['course'] = parent_course
    except Question.DoesNotExist:
        context_dict['answers'] = None
        context_dict['question'] = None
        context_dict['subject'] = None
        context_dict['course'] = None

    return render(request,'gliocas_app/question.html', context = context_dict)

def search(request):
    result_list=[]
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            result_list = search_query(query)
        return render(request,'gliocas_app/search.html', {'result_list': result_list,
                                                          "user_query" : query})
    return render(request,'gliocas_app/search.html', {'result_list': result_list})

@login_required
def add_question(request, subject_slug, course_slug):
    
    form = QuestionForm()
    try:
        course = Course.objects.get(slug=course_slug)
        user = request.user
    except (Course.DoesNotExist, User.DoesNotExist):
        course = None
        user = None
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            if course and user:
                question = form.save(commit=False)
                question.course = course
                question.poster = user
                question.views = 0
                question.save()
                return show_question(request, subject_slug, course_slug, question.slug)
        else:
            print(form.errors)

    context_dict = {}
    context_dict['form'] = form
    context_dict['subject'] = Subject.objects.get(slug=subject_slug)
    context_dict['course'] = Course.objects.get(slug=course_slug)
    return render(request,'gliocas_app/add_question.html', context = context_dict)

@user_passes_test(lambda u: u.is_superuser)
def add_course(request, subject_slug):
    form = CourseForm()
    try:
        subject = Subject.objects.get(slug=subject_slug)
    except (Subject.DoesNotExist):
        subject = None
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            if subject:
                course = form.save(commit=False)
                course.subject = subject
                course.save()
                return show_course(request, subject_slug, course.slug)
        else:
            print(form.errors)
    context_dict = {}
    context_dict['form'] = form
    context_dict['subject'] = Subject.objects.get(slug=subject_slug)
    return render(request,'gliocas_app/add_course.html', context = context_dict)

@user_passes_test(lambda u: u.is_superuser)
def add_subject(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save()
            return show_subject(request, subject.slug)
        else:
            print(form.errors)
    context_dict = {}
    context_dict['form'] = form
    return render(request,'gliocas_app/add_subject.html', context = context_dict)

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

@login_required
def like_question(request, subject_slug, course_slug, question_slug, like):
    question = get_object_or_404(Question, slug = question_slug)
    user = request.user
    try: 
        upvote = UpvoteQuestion.objects.get(question=question, user=user)
    except UpvoteQuestion.DoesNotExist:
        upvote = None
    if upvote != None:
        if upvote.positive and (like == '1'):
            UpvoteQuestion.objects.get(question=question, user=user).delete()
        elif not upvote.positive and (like == '0'):
            UpvoteQuestion.objects.get(question=question, user=user).delete()
        else:
            upvote.positive = not upvote.positive
            upvote.save()
    else:
        upvote = UpvoteQuestion.objects.create(question=question, user=user, positive=(like == '1'))
        upvote.save()
    return show_question(request, subject_slug, course_slug, question_slug)

@login_required
def like_answer(request, subject_slug, course_slug, question_slug, answer_key, like):
    answer = Answer.objects.get(pk=answer_key)
    user = request.user
    try: 
        upvote = UpvoteAnswer.objects.get(answer=answer, user=user)
    except UpvoteAnswer.DoesNotExist:
        upvote = None
    if upvote != None:
        if upvote.positive and (like == '1'):
            UpvoteAnswer.objects.get(answer=answer, user=user).delete()
        elif not upvote.positive and (like == '0'):
            UpvoteAnswer.objects.get(answer=answer, user=user).delete()
        else:
            upvote.positive = not upvote.positive
            upvote.save()
    else:
        upvote = UpvoteAnswer.objects.create(answer=answer, user=user, positive=(like == '1'))
        upvote.save()
    return show_question(request, subject_slug, course_slug, question_slug)

@login_required
def like_reply(request, subject_slug, course_slug, question_slug, reply_key, like):
    reply = Reply.objects.get(pk = reply_key)
    user = request.user
    try: 
        upvote = UpvoteReply.objects.get(reply=reply, user=user)
    except UpvoteReply.DoesNotExist:
        upvote = None
    if upvote != None:
        if upvote.positive and (like == '1'):
            UpvoteReply.objects.get(reply=reply, user=user).delete()
        elif not upvote.positive and (like == '0'):
            UpvoteReply.objects.get(reply=reply, user=user).delete()
        else:
            upvote.positive = not upvote.positive
            upvote.save()
    else:
        upvote = UpvoteReply.objects.create(reply=reply, user=user, positive=(like == '1'))
        upvote.save()
    return show_question(request, subject_slug, course_slug, question_slug)

@login_required
def answer_question(request, subject_slug, course_slug, question_slug):
    form = AnswerForm()
    try:
        course = Course.objects.get(slug=course_slug)
        user = request.user
        question = Question.objects.get(slug=question_slug)
    except (Course.DoesNotExist, User.DoesNotExist, Question.DoesNotExist):
        course = None
        user = None
        question = None
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            if course and user and question:
                answer = form.save(commit=False)
                answer.poster = user
                answer.question = question
                answer.save()
                return show_question(request, subject_slug, course_slug, question_slug)
        else:
            print(form.errors)

    context_dict = {}
    context_dict['form'] = form
    context_dict['subject'] = Subject.objects.get(slug=subject_slug)
    context_dict['course'] = Course.objects.get(slug=course_slug)
    context_dict['question'] = question
    return render(request,'gliocas_app/answer_question.html', context = context_dict)


@login_required
def reply_answer(request, subject_slug, course_slug, question_slug, answer_key):
    form = ReplyForm()
    try:
        course = Course.objects.get(slug=course_slug)
        user = request.user
        question = Question.objects.get(slug=question_slug)
        answer = Answer.objects.get(pk=answer_key)
    except (Course.DoesNotExist, User.DoesNotExist, Question.DoesNotExist, Answer.DoesNotExist):
        course = None
        user = None
        answer = None
        question = None
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            if course and user and answer:
                reply = form.save(commit=False)
                reply.poster = user
                reply.answer = answer
                reply.save()
                return show_question(request, subject_slug, course_slug, question_slug)
        else:
            print(form.errors)

    context_dict = {}
    context_dict['form'] = form
    context_dict['subject'] = Subject.objects.get(slug=subject_slug)
    context_dict['course'] = Course.objects.get(slug=course_slug)
    context_dict['question'] = Question.objects.get(slug=question_slug)
    context_dict['answer'] = Answer.objects.get(pk=answer_key)
    context_dict['replies'] = Reply.objects.filter(answer=answer)
    return render(request,'gliocas_app/reply_answer.html', context = context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user(request, username):
    context_dict = {'username' : username}
    try:
        user = User.objects.get(username = username)
        context_dict['exists'] = True
        context_dict['searched_user'] = user
        context_dict['numquestions'] = len(Question.objects.filter(poster = user))
        context_dict['numanswers'] = len(Answer.objects.filter(poster = user))
    except User.DoesNotExist:
        context_dict['exists'] = False

    return render(request, 'gliocas_app/user.html', context_dict)


def user_questions(request, username):
    context_dict = {'username' : username, 'objectname' : 'questions'}
    try:
        user = User.objects.get(username = username)
        context_dict['exists'] = True
        context_dict['searched_user'] = user
        context_dict['questions'] = Question.objects.filter(poster = user)
    except User.DoesNotExist:
        context_dict['exists'] = False
    
    return render(request, 'gliocas_app/user_questions.html', context_dict)

def user_answers(request, username):
    context_dict = {'username' : username, 'objectname' : 'answers'}
    try:
        user = User.objects.get(username = username)
        context_dict['exists'] = True
        context_dict['searched_user'] = user
        context_dict['questions'] = [ answer.question for answer in  Answer.objects.filter(poster = user) ]
    except User.DoesNotExist:
        context_dict['exists'] = False
    
    return render(request, 'gliocas_app/user_questions.html', context_dict)
