import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gliocas.settings')

import django
django.setup()
from django.contrib.auth.models import User
from gliocas_app.models import Subject, Course, Question, Answer, Reply
from gliocas_app.models import UpvoteQuestion, UpvoteAnswer, UpvoteReply

def populate():
    users = {"random_boy" : add_user("random_boy"),
             "space_pilot" : add_user("space_pilot"),
             "fresher671" : add_user("fresher671"),
             "python_boy" : add_user("python_boy"),
             "rango" : add_user("rango"),
             "proudScottish" : add_user("proudScottish"),
             "the_senate" : add_user("the_senate"),
             "helpful_student" : add_user("helpful_student"),
             "boromir" : add_user("boromir")}
    maths2c_questions = [
        {"title" : "I don't understand dimensions",
         "text" : "HELP I DON'T GET THIS AND IM GONNA FAIL",
         "poster" : users["random_boy"],
         "views" : 10,
         "upvotes" : [],
         "downvotes" : [],
         "answers" : {}},
        {"title" : "On the subject of acceleration",
         "text" : "Should I try spinning? I've heard it's a good trick",
         "poster" : users["space_pilot"],
         "views" : 501,
         "upvotes" : [users["the_senate"], users["random_boy"],
                      users["space_pilot"], users["boromir"],
                      users["helpful_student"], users["proudScottish"]],
         "downvotes" : [],
         "answers" : [
             {"text" : "DO IT",
              "poster" : users["the_senate"],
              "upvotes" : [users["the_senate"], users["random_boy"],
                           users["space_pilot"], users["boromir"],
                           users["helpful_student"], users["proudScottish"]],
              "downvotes" : [],},
             ]},
        ]
    maths1r_questions = [
        {"title" : "How do I solve quadratic equations?",
         "text" : ("Basically, I have the equation x^2 + x - 2 = 0 and I"
                   " don't know how to solve it"),
         "poster" : users["fresher671"],
         "views" : 7,
         "upvotes" : [users["fresher671"], users["random_boy"]],
         "downvotes" : [users["the_senate"], users["space_pilot"],
                        users["boromir"]],
         "answers" : {}},
        {"title" : "Can anyone explain me differentiation?",
         "text" : "It's hard, I don't get it",
         "poster" : users["fresher671"],
         "views" : 420,
         "upvotes" : [],
         "downvotes" : [users["the_senate"], users["random_boy"],
                        users["space_pilot"], users["boromir"],
                        users["proudScottish"]],
         "answers" : [
             {"text" : "Wait for integration, you'll have some laughts",
              "poster" : users["the_senate"],
              "upvotes" : [users["the_senate"], users["random_boy"],
                           users["space_pilot"], users["boromir"],
                           users["proudScottish"]],
              "downvotes" : [],},
             ]},
        ]
    maths3h_questions = []
    maths2a_questions = []
    oose_questions = [
        {"title" : "Why is if(string==string a bug pattern?)",
         "text" : ("I don't get why making a comparison between two strings"
                   " is a bug pattern according to SpotBugs. Please help"
                   " I need to finish this for tomorrow"),
         "poster" : users["python_boy"],
         "views" : 49,
         "upvotes" : [users["python_boy"], users["helpful_student"]],
         "downvotes" : [users["the_senate"],users["space_pilot"],
                        users["boromir"]],
         "answers" : [
             {"text" : ("In Java strings are objects, so if you want to"
                        " compare two string you need to use"
                        " string1.equals(string2)"),
              "poster" : users["helpful_student"],
              "upvotes" : [users["python_boy"]],
              "downvotes" : [],},
             ]},
        ]
    wad_questions = [
        {"title" : "I have to create a webpage how do I do it?",
         "text" : ("I'm in a group project and we need to create a website"
                   " for tomorrow and we don't know what to do. Any ideas"),
         "poster" : users["rango"],
         "views" : 123,
         "upvotes" : [users["rango"]],
         "downvotes" : [users["the_senate"], users["random_boy"],
                        users["space_pilot"], users["boromir"],
                        users["proudScottish"]],
         "answers" : [
             {"text" : "One does not simply create a website",
              "poster" : users["boromir"],
              "upvotes" : [users["the_senate"], users["random_boy"],
                           users["space_pilot"], users["boromir"],
                           users["proudScottish"]],
              "downvotes" : [users["rango"]],},
             ]},
        ]
    cs1p_questions = []
    cs1q_questions = []
    burns_questions = [
        {"title" : "Who's this guy?",
         "text" : ("I took this subject and I have no idea about what"
                   " we are doing. Can anyone tell me, to begin with,"
                   " who is this Robert Burns?"),
         "poster" : users["proudScottish"],
         "views" : 17,
         "upvotes" : [],
         "downvotes" : [],
         "answers" : {}},
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
               "History" : history_courses,
                "Economics" : {}}

    for subject in Subjects:
        s = add_subject(subject)
        for course in Subjects[subject]:
            c = add_course(course, s)
            for question in Subjects[subject][course]:
                q = add_question(question["title"], question["text"],
                                 c, question["poster"], question["views"])
                for upvote in question["upvotes"]:
                    add_upvoteQuestion(q, upvote, True)
                for downvote in question["downvotes"]:
                    add_upvoteQuestion(q, downvote, False)
                for answer in question["answers"]:
                    a = add_answer(answer["text"], q, answer["poster"])
                    for upvote in answer["upvotes"]:
                        add_upvoteAnswer(a, upvote, True)
                    for downvote in answer["downvotes"]:
                        add_upvoteAnswer(a, downvote, False)

    for s in Subject.objects.all():
        print("subject " + str(s) + ":")
        for c in Course.objects.filter(subject=s):
            print("\tcourse " + str(c) + ":")
            for q in Question.objects.filter(course=c):
                print("\t\t", "title", q.title)
                print("\t\t", "text", q.text)
                print("\t\t", "poster", q.poster)
                print("\t\t", "date", q.date)
                print("\t\t", "views", q.views)
                upvotes = 0
                for q_up in UpvoteQuestion.objects.filter(question=q):
                    if q_up.positive == True:
                        upvotes = upvotes + 1
                    else:
                        upvotes = upvotes - 1
                print("\t\t", "upvotes", upvotes)
                for a in Answer.objects.filter(question=q):
                    print("\t\t\t", "text", a.text)
                    print("\t\t\t", "poster", a.poster)
                    print("\t\t\t", "date", a.date)
                    upvotes = 0
                    for a_up in UpvoteAnswer.objects.filter(answer=a):
                        if a_up.positive == True:
                            upvotes = upvotes + 1
                        else:
                            upvotes = upvotes - 1
                    print("\t\t\t", "upvotes", upvotes)


def add_user(name):
    user = User.objects.get_or_create(username=name)[0]
    user.email = 'email@email.com'
    user.password = 'password'
    user.save()
    return user

def add_subject(name):
    subject = Subject.objects.get_or_create(name=name)[0]
    subject.save()
    return subject

def add_course(name, subject):
    course = Course.objects.get_or_create(name=name, subject=subject)[0]
    course.save()
    return course

def add_question(title, text, course, poster, views=0):
    question = Question.objects.get_or_create(course=course, poster=poster,
                                              title=title)[0]
    question.date = datetime.datetime.now()
    question.text = text
    question.views = views
    question.save()
    return question

def add_answer(text, question, poster):
    answer = Answer.objects.get_or_create(question=question,
                                          poster=poster, text=text)[0]
    answer.date = datetime.datetime.now()
    answer.save()
    return answer

def add_upvoteQuestion(question, user, positive=True):
    upvote = UpvoteQuestion.objects.get_or_create(question=question,
                                                  user=user)[0]
    upvote.positive = positive
    upvote.save()
    return upvote

def add_upvoteAnswer(answer, user, positive=True):
    upvote = UpvoteAnswer.objects.get_or_create(answer=answer, user=user)[0]
    upvote.positive = positive
    upvote.save()
    return upvote

def add_upvoteReply(reply, user, positive=True):
    upvote = UpvoteReply.objects.get_or_create(reply=reply, user=user)[0]
    upvote.positive = positive
    upvote.save()
    return upvote


# Start execution here!
if __name__=='__main__':
    print("Starting Gliocas population script...")
    populate()
