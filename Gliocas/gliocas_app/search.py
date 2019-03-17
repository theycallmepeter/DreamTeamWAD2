from gliocas_app.models import Subject, Course, Question, UpvoteQuestion

def search_query(query):
    invalidCharacters = [".", ",", ":", ";", "?", "'", "!", "-", "_"]
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
            elif len(word) > 3:
                for titleWord in question["title"]:
                    if len(titleWord) > 3 and (titleWord in word or word in titleWord):
                       question["titleWords"] += 0.5 
            if word in question["text"]:
                question["textWords"] += 1

    for question in questionsData:
        question["queryOrder"] = 10*question["titleWords"] + question["textWords"]

    results = []
    for i in range(0, len(questionsData)):
        position = 0
        value = 0
        for j in range(0, len(questionsData)):
            if questionsData[j]["queryOrder"] > value:
                position = j
                value = questionsData[j]["queryOrder"]
        primaryKey = questionsData[position]["pk"]
        if value > 0:
            results.append(Question.objects.filter(pk=primaryKey)[0])
        del questionsData[position]
    return results
