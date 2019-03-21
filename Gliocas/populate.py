import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gliocas.settings')

import django
django.setup()
from django.utils import timezone
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
             "boromir" : add_user("boromir"),
             "historyNerd" : add_user("historyNerd")}
    
    maths2c_questions = [
        {"title" : "I don't understand dimensions",
         "text" : "HELP I DON'T GET THIS AND IM GONNA FAIL",
         "poster" : users["random_boy"],
         "views" : 10,
         "upvotes" : [],
         "downvotes" : [users["proudScottish"], users["rango"]],
         "answers" : [
             {"text" : ("My God, thats like the easiest thing in the course."
                        " If you can't understand this you should drop man"),
              "poster" : users["proudScottish"],
              "upvotes" : [users["rango"], users["proudScottish"]],
              "downvotes" : [],
              "replies" : []},
             ]},
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
              "downvotes" : [],
              "replies" : []},
             {"text" : "My lord, is that legal?",
              "poster" : users["boromir"],
              "upvotes" : [users["the_senate"], users["random_boy"],
                           users["space_pilot"], users["the_senate"],
                           users["helpful_student"], users["proudScottish"]],
              "downvotes" : [],
              "replies" : [
                  {"text" : "I will make it legal",
                   "poster" : users["the_senate"],
                   "upvotes": [users["boromir"], users["helpful_student"],
                               users["space_pilot"]],
                   "downvotes" : []},
                  ]},
             ]},
        ]
    
    maths1r_questions = [
        {"title" : "How do I solve quadratic equations?",
         "text" : ("Basically, I have the equation $$x^2 + x - 2 = 0$$ and I"
                   " don't know how to solve it."),
         "poster" : users["fresher671"],
         "views" : 7,
         "upvotes" : [users["fresher671"], users["random_boy"]],
         "downvotes" : [users["the_senate"], users["space_pilot"],
                        users["boromir"]],
         "answers" : [
             {"text" : ("I shouldn't need to explain this to a maths student but"
                        " here we go: for a quadratic equation of the form "
                        "$$ax^2 + bx + c = 0$$ the solution is "
                        "$$x = \frac{-b\pm\sqrt{a^2-4ac}}{2a}$$ "
                        "In your case the solution would be x = 1 "
                        "and x = -2"),
              "poster" : users["helpful_student"],
              "upvotes" : [users["fresher671"], users["random_boy"]],
              "downvotes" : [],
              "replies" : []},
             ]},
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
              "downvotes" : [],
              "replies" : []},
             ]},
        ]
    
    maths3h_questions = []
    maths2a_questions = []
    
    oose_questions = [
        {"title" : "Why is if(string==string) a bug pattern?",
         "text" : ("I don't get why making a comparison between two strings"
                   " is a bug pattern according to SpotBugs. Please help"
                   " I need to finish this for tomorrow"),
         "poster" : users["python_boy"],
         "views" : 49,
         "upvotes" : [users["python_boy"], users["helpful_student"],
                      users["the_senate"], users["space_pilot"],
                      users["boromir"]],
         "downvotes" : [],
         "answers" : [
             {"text" : ("In Java strings are objects, so if you want to"
                        " compare two string you need to use"
                        " string1.equals(string2)."),
              "poster" : users["helpful_student"],
              "upvotes" : [users["python_boy"], users["boromir"],
                           users["helpful_student"], users["the_senate"]],
              "downvotes" : [],
              "replies" : [
                  {"text" : ("This answer is basically the answer. Just to "
                             "clarify that this is the case with everything"
                             " in Java, except for primitives like int or char,"
                             " as except for prmitives every single thing in "
                             "Java is an object."),
                   "poster" : users["boromir"],
                   "upvotes": [users["the_senate"], users["helpful_student"],
                               users["python_boy"]],
                   "downvotes" : []},
                  ]},
             ]},
        ]
    
    wad_questions = [
        {"title" : "I have to create a webpage how do I do it?",
         "text" : ("I'm in a group project and we need to create a website"
                   " for tomorrow and we don't know what to do. Any ideas?"),
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
              "downvotes" : [users["rango"]],
              "replies" : []},
             ]},
        {"title" : "How do I implement user login in my webpage?",
         "text" : ("I have almost completed the assignment for next Friday,"
                   " but I am totally clueless about letting users create"
                   " accounts and login in"),
         "poster" : users["boromir"],
         "views" : 420,
         "upvotes" : [users["the_senate"], users["random_boy"],
                      users["space_pilot"], users["boromir"],
                      users["proudScottish"]],
         "downvotes" : [users["rango"]],
         "answers" : [
             {"text" : ("One doesn't create a login or whatever you"
                        " answered to my question"),
              "poster" : users["rango"],
              "upvotes" : [],
              "downvotes" : [users["boromir"]],
              "replies" : [
                  {"text" : ("You can not even quote me correctly, it's "
                             "literally copying and pasting"),
                   "poster" : users["boromir"],
                   "upvotes": [users["the_senate"]],
                   "downvotes" : []},
                  ]},
             {"text" : ("TangoWithDjango has a sept-by-step solution for that"
                        " problem. If you are still struggling, you can always"
                        " use the django-registration-redux package to take"
                        " care of all the user login stuff. Hope that you"
                        " find this useful!"),
              "poster" : users["helpful_student"],
              "upvotes" : [users["boromir"], users["the_senate"],
                           users["proudScottish"], users["space_pilot"]],
              "downvotes" : [],
              "replies" : []},
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
    ww2_questions = [
        {"title" : "Who was Latin America supporting during WWII?",
         "text" : ("I was given an assignment about the different alliances "
                   "during the war and although I pretty much know who was "
                   "with who in Europe and Asia, I have no idea about the "
                   "participation in the war of Latin American countries like"
                   " Mexico or Brazil. Did they participated during WWII at "
                   "all?"),
         "poster" : users["historyNerd"],
         "views" : 1942,
         "upvotes" : [users["python_boy"], users["helpful_student"],
                      users["the_senate"], users["space_pilot"],
                      users["boromir"]],
         "downvotes" : [],
         "answers" : [
             {"text" : ("They mostly supported the Allies, although bar Brazil "
                        "they didn't send troops to Europe. However, there "
                        "were skirmishes between Latin American and Axis boats"
                        " and submarines during the war"),
              "poster" : users["helpful_student"],
              "upvotes" : [users["historyNerd"], users["helpful_student"],
                           users["the_senate"], users["space_pilot"],
                           users["boromir"]],
              "downvotes" : [],
              "replies" : [
                  {"text" : ("Great answer! However don't forget about the "
                             "300 volunteers that Mexico sent to the Pacific "
                             " Theatre, known as the Águilas Aztecas"),
                   "poster" : users["the_senate"],
                   "upvotes": [users["the_senate"], users["helpful_student"],
                               users["historyNerd"], users["boromir"]],
                   "downvotes" : []},
                  ]},
             {"text" : ("They were Hitler's puppets and contries like Mexico "
                        "planned to help Germany invade the US in exchange for"
                        " the lost territories in the 1748 war. Others like "
                        " Argentina gave asylum to Hitler himself when he lost"
                        " the war and help him cover his tracks and get a new"
                        " identity."),
              "poster" : users["random_boy"],
              "upvotes" : [],
              "downvotes" : [users["historyNerd"], users["helpful_student"],
                             users["the_senate"], users["space_pilot"],
                             users["boromir"]],
              "replies" : [
                  {"text" : ("This is one of the most stupid things I've ever "
                             "read on this website. Either you get the facts "
                             "wrong or you just talk conspiracy nonsense. For"
                             " starters, Germany offered Mexico US land in "
                             "WW1, not WW2, and Mexico never accepted the "
                             "proposal. Also, the war you are talking about "
                             "took place between 1846 and 1848, not in 1748."
                             " That year neither Mexico not the US existed at"
                             " all. Also, although some high profile Nazis "
                             "escaped to Argentina, Hitler wasn't one of them."
                             " He committed suicide. Stop spreading "
                             "misinformation!"),
                   "poster" : users["helpful_student"],
                   "upvotes": [users["the_senate"], users["helpful_student"],
                               users["historyNerd"], users["boromir"]],
                   "downvotes" : []},
                  {"text" : ("Fake news!"),
                   "poster" : users["boromir"],
                   "upvotes": [],
                   "downvotes" : []},
                  {"text" : ("Amazing. Every word of what you just said was "
                             "wrong."),
                   "poster" : users["space_pilot"],
                   "upvotes": [users["the_senate"],],
                   "downvotes" : []},
                  ]},
             ]},
        ]
    
    ancientHistory_questions = [
        {"title" : "Did any of you hear the Tragedy of MacPlagueis the Wise?",
         "text" : ("Im trying to find information about this guy, but this is"
                   " not a story the lecturers would tell me."),
         "poster" : users["space_pilot"],
         "views" : 999,
         "upvotes" : [users["the_senate"], users["random_boy"],
                      users["space_pilot"], users["boromir"],
                      users["proudScottish"]],
         "downvotes" : [],
         "answers" : [
             {"text" : ("I thought not. It's a highlander legend. MacPlagueis "
                        "was a clan chief of Scotland, so powerful and so wise"
                        " he could use the thistles to influence the Scots to "
                        "follow him... He had such a knowledge of the herbs "
                        "powers that he could even unite all of the clans and "
                        "be the king of Scotland. The ancient rituals of the "
                        "druids are a pathway to many abilities some consider "
                        "to be unnatural. He became so powerful... the only "
                        "thing he was afraid of was losing his power, which "
                        "eventually, of course, he did. Unfortunately, he taught"
                        " his son everything he knew, then his son"
                        " killed him in his sleep. It's ironic, he could control"
                        " everyone except for his very own family."),
              "poster" : users["the_senate"],
              "upvotes" : [users["boromir"], users["the_senate"],
                           users["proudScottish"], users["space_pilot"],
                           users["random_boy"], users["fresher671"],
                           users["python_boy"], users["rango"]],
              "downvotes" : [users["helpful_student"]],
              "replies" : [
                  {"text" : ("Oh this looks so cool. Is it possible to learn "
                             "this power?"),
                   "poster" : users["proudScottish"],
                   "upvotes": [users["the_senate"]],
                   "downvotes" : []},
                  {"text" : ("Nonsense. As I said in my answer, this is nothing "
                             "more than a mere legend, and not an interesting "
                             "one to be honest."),
                   "poster" : users["helpful_student"],
                   "upvotes": [],
                   "downvotes" : [users["the_senate"], users["space_pilot"]]},
                  ]},
             ]},
        ]
    
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
    
    history_courses = {"World War II" : ww2_questions,
                       "Ancient history" : ancientHistory_questions}
    
    economics_courses = {}
    politics_courses = {}

    Subjects = {"Mathematics" : math_courses,
                "Computing Science" : compSci_courses,
                "Literature" : literature_courses,
                "Gender Studies" : genderStudies_courses,
                "History" : history_courses,
                "Economics" : economics_courses,
                "Politics" : politics_courses}

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
                    for reply in answer["replies"]:
                        r = add_reply(reply["text"], a, reply["poster"])
                        for upvote in reply["upvotes"]:
                            add_upvoteReply(r, upvote, True)
                        for downvote in reply["downvotes"]:
                            add_upvoteReply(r, downvote, False)

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
                    
                    for r in Reply.objects.filter(answer=a):
                        print("\t\t\t\t", "text", r.text)
                        print("\t\t\t\t", "poster", r.poster)
                        print("\t\t\t\t", "date", r.date)
                        upvotes = 0
                        for r_up in UpvoteReply.objects.filter(reply=r):
                            if r_up.positive == True:
                                upvotes = upvotes + 1
                            else:
                                upvotes = upvotes - 1
                        print("\t\t\t\t", "upvotes", upvotes)

    admin = User.objects.get_or_create(username='admin',is_staff=True,is_superuser=True)[0]
    admin.email = 'admin@admin.com'
    admin.password = 'admin'
    admin.set_password(admin.password)
    admin.save()

    defaultUser = User.objects.get_or_create(username='Deleted')[0]
    defaultUser.email = 'obiwan@kenobi.com'
    defaultUser.password = 'High ground'
    defaultUser.set_password(defaultUser.password)
    defaultUser.save()


    admin = User.objects.get_or_create(username='admin',is_staff=True,is_superuser=True)[0]
    admin.email = 'admin@admin.com'
    admin.password = 'admin'
    admin.set_password(admin.password)
    admin.save()



def add_user(name):
    user = User.objects.get_or_create(username=name)[0]
    user.email = 'email@email.com'
    user.password = 'password'
    user.set_password(user.password)
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
    question.date = timezone.now()
    question.text = text
    question.views = views
    question.save()
    return question

def add_answer(text, question, poster):
    answer = Answer.objects.get_or_create(question=question, poster=poster,
                                          text=text)[0]
    answer.date = timezone.now()
    answer.save()
    return answer

def add_reply(text, answer, poster):
    reply = Reply.objects.get_or_create(answer=answer, poster=poster,
                                        text=text)[0]
    reply.date = timezone.now()
    reply.save()
    return reply

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
