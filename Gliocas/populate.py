import datetime
import hashlib
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gliocas.settings')

import django
django.setup()
from django.contrib.auth.models import User
from gliocas_app.models import Subject, Course, Question
from gliocas_app.models import Answer, Reply, UserProfile

def populate():
    user = UserProfile.objects.create_user('john',
                                           'lennon@thebeatles.com', 'johnpassword')
    user.save()
    maths2c_questions = [
        {"title" : "I don't understand dimensions",
         "text" : "HELP I DON'T GET THIS AND IM GONNA FAIL",
         "poster" : "random_boy"},
        {"title" : "On the subject of acceleration",
         "text" : "Should I try spinning? I've heard it's a good trick",
         "poster" : "space_pilot"},
        ]
    maths1r_questions = [
        {"title" : "How do I solve quadratic equations?",
         "text" : ("Basically, I have the equation x^2 + x - 2 = 0 and I"
                   " don't know how to solve it"),
         "poster" : "fresher671"},
        {"title" : "Can anyone explain me differentiation?",
         "text" : "It's hard, I don't get it",
         "poster" : "fresher671"},
        ]
    maths3h_questions = []
    maths2a_questions = []
    oose_questions = [
        {"title" : "Why is if(string==string a bug pattern?)",
         "text" : ("I don't get why making a comparison between two strings"
                   " is a bug pattern according to SpotBugs. Please help"
                   " I need to finish this for tomorrow"),
         "poster" : "python_boy"},
        ]
    wad_questions = [
        {"title" : "I have to create a webpage how do I do it?",
         "text" : ("I don't get why making a comparison between two strings"
                   " is a bug pattern according to SpotBugs. Please help"
                   " I need to finish this for tomorrow"),
         "poster" : "rango"},
        ]
    cs1p_questions = []
    cs1q_questions = []
    burns_questions = [
        {"title" : "Who's this guy?",
         "text" : ("I took this subject and I have no idea about what"
                   " we are doing. Can anyone tell me, to begin with,"
                   " who is this Robert Burns?"),
         "poster" : "proudScottish"},
        ]
    genderHistory_questions = []
    spanishHistory_questions = []
    
    math_courses = {"2C" : maths2c_questions,
                   "1R" : maths1r_questions,
                   "3H" : maths3h_questions,
                   "2A" : maths2a_questions}
    compSci_courses = {"OOSE" : oose_questions,
                       "WAD 2" : wad_questions,
                       "CS-1P" : cs1p_questions,
                       "CS-1Q" : cs1q_questions}
    literature_courses = {"Robert Burns" : burns_questions}
    genderStudies_courses = {"History of oppression" : genderHistory_questions}
    history_courses = {"The empire where the sun never sets" : spanishHistory_questions}

    Subjects = {"Mathematics" : math_courses,
               "Computing Science" : compSci_courses,
               "Literature" : literature_courses,
               "Gender Studies" : genderStudies_courses,
               "History" : history_courses}

    for subject in Subjects:
        s = add_subject(subject)
        for course in Subjects[subject]:
            c = add_course(course, s)
            '''
            for question in Subjects[subject][course]:
                q = add_question(question["title"], question["text"],
                             c, question["poster"])
            '''

    for s in Subject.objects.all():
        print("subject " + str(s) + ":")
        for c in Course.objects.filter(subject=s):
            print("\tcourse " + str(c) + ":")
            '''
            for q in Question.objects.filter(course=c):
                print("\t\t{0} - {1} - {2}".format(str(s),str(c),str(q)))
            '''


def add_subject(name):
    subject = Subject.objects.get_or_create(name=name)[0]
    subject.save()
    return subject

def add_course(name, subject):
    course = Course.objects.get_or_create(name=name, subject=subject)[0]
    course.save()
    return course

def add_question(title, text, course, poster):
    question = Question.objects.get_or_create(course=course, poster=poster)[0]
    question.title = title
    question.text = text
    question.date = datetime.datetime.now()
    question.save()
    return question


# Start execution here!
if __name__=='__main__':
    print("Starting Gliocas population script...")
    populate()
