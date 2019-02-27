import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gliocas.settings')

import django
django.setup()
from gliocas.models import Subject, Course, Question

def populate():
    
    OOSE2ques = ['I love Inahs hair', 'We need more workshops']
    ADS2ques = ['Red-black tree is racist','Is there git mergesort']
    WAD2ques = ['Manlove appreciation thread','Looking for tango lessons','Did you know Gliocas was a WAD2 project!?']

    Math2Eques = ['am converging to suicide','am at my limit','is this number even real']
    Math2Dques = ['does watching The Matrix count as revision']
    Math2Cques = [] #empty on purpose

    CScourses = { 'OOSE2' : OOSE2ques, 'ADS2' : ADS2ques, 'WAD2': WAD2ques }
    Mathcourses = { '2E' : Math2Eques, '2C' : Math2Cques, '2D' :Math2Dques }
    Gendercourses = {} #empty on purpose

    Subjects = {'CS' : CScourses, 'Math' : Mathcourses, 'Gender studies' : Gendercourses }

    for subject,courses in Subjects.items():
        s = add_subject(subject)
        for course,questions in Subjects[subject].items():
            c = add_course(s, course)
            for question in questions:
                add_question(s,c,question)

    # Print out what we added

    for s in Subject.objects.all():
        print("subject " + str(s) + ":")
        for c in Course.objects.filter(subject=s):
            print("\tcourse " + str(c) + ":")
            for q in Question.objects.filter(course=c):
                print("\t\t{0} - {1} - {2}".format(str(s),str(c),str(q)))

def add_subject(subject):
    s = Subject.objects.get_or_create(name=subject)[0]
    s.save()
    return s

def add_course(subject,course):
    c = Course.objects.get_or_create(subject=subject,name=course)[0]
    c.save()
    return c

def add_question(subject, course, question):
    q = Question.objects.get_or_create(subject=subject,course=course,title=question)[0]
    q.save()
    return q
     
# Start execution here!
if __name__ == '__main__':
    print("Starting Gliocas population script...")
    populate()
