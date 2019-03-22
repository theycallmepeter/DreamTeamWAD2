from gliocas_app.models import Subject, Course, Question, UpvoteQuestion, UpvoteAnswer, UpvoteReply, Subject, Answer, Reply, Followed
from django import template
from django.contrib.auth.models import User

register = template.Library()

def score(votes):
    score = sum([ 1 if vote.positive else -1 for vote in votes ])
    return score

@register.simple_tag
def questionscore(question):
    return score(UpvoteQuestion.objects.filter(question = question))

@register.simple_tag
def answerscore(answer):
    return score(UpvoteAnswer.objects.filter(answer = answer))

@register.simple_tag
def replyscore(reply):
    return score(UpvoteReply.objects.filter(reply = reply))

#Deprecated
@register.simple_tag
def questionVoted(question, user):
    is_voted = UpvoteQuestion.objects.filter(question = question, user=user).exists()
    if is_voted:
        vote = UpvoteQuestion.objects.get(question = question, user=user)
        if vote.positive:
            return True
        else:
            return False
    return None

#Deprecated
@register.simple_tag
def answerVoted(answer, user):
    is_voted = UpvoteAnswer.objects.filter(answer = answer, user=user).exists()
    if is_voted:
        vote = UpvoteAnswer.objects.get(answer = answer, user=user)
        if vote.positive:
            return 'upvoted'
        else:
            return 'downvoted'
    return None

#Deprecated
@register.simple_tag
def replyVoted(reply, user):
    is_voted = UpvoteReply.objects.filter(reply = reply, user=user).exists()
    if is_voted:
        vote = UpvoteReply.objects.get(reply = reply, user=user)
        if vote.positive:
            return 'upvoted'
        else:
            return 'downvoted'
    return None
