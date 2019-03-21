from gliocas_app.models import Subject, Course, Question, UpvoteQuestion, UpvoteAnswer, UpvoteReply, Subject, Answer, Reply, Followed
from django import template

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
