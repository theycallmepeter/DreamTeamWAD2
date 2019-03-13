import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gliocas.settings')

import django
django.setup()
from gliocas_app.models import Subject, Course, Question, UpvoteQuestion

def search(query):
    invalidCharacters = [".", ",", ":", ";", "?", "'", "!"]
    query_words = query.split()
    for i in range(0, len(query_words)):
        query_words[i] = query_words[i].lower()
        for character in invalidCharacters:
            query_words[i] = query_words[i].replace(character, '')
    
    questions = Question.objects.all()
    questionsData = []
    for question in questions:
        questionTitle = question.title.split()
        for i in range(0, len(questionTitle)):
            questionTitle[i] = questionTitle[i].lower()
            for character in invalidCharacters:
                questionTitle[i] = questionTitle[i].replace(character, '')
        questionText = question.text.split()
        for i in range(0, len(questionText)):
            questionText[i] = questionText[i].lower()
            for character in invalidCharacters:
                questionText[i] = questionText[i].replace(character, '')
        questionsData.append({"pk" : question.pk, "title" : questionTitle,
                              "text" : questionText,
                              "titleWords" : 0, "textWords" : 0,
                              "queryOrder" : 0})

    for word in query_words:
        for question in questionsData:
            if word in question["title"]:
                question["titleWords"] += 1
            if word in question["text"]:
                question["textWords"] += 1

    for question in questionsData:
        question["queryOrder"] = 10*question["titleWords"] + question["textWords"]

    results = []
    last_value = 10
    if len(questionsData) < 10:
        last_value = len(questionsData)
    for i in range(0, last_value):
        position = 0
        a = questionsData[0]
        value = questionsData[0]["queryOrder"]
        for j in range(0, len(questionsData)):
            if questionsData[j]["queryOrder"] > value:
                position = j
                value = questionsData[j]["queryOrder"]
        results.append(questionsData[position]["pk"])
        del questionsData[position]
    
    return results
