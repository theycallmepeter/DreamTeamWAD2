from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

def get_sentinel_user():
    user = User.objects.get_or_create(username='Deleted')[0]
    user.email = 'obiwan@kenobi.com'
    user.password = 'High ground'
    return user

'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
'''

class Subject(models.Model):
    maxLength = 64
    name = models.CharField(max_length=maxLength, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    maxLength = 64
    name = models.CharField(max_length=maxLength, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    titleLength = 256
    textLength = 32768
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    poster = models.ForeignKey(User,
                               on_delete=models.SET(get_sentinel_user))
    title = models.CharField(max_length=titleLength)
    text = models.TextField(max_length=textLength)
    date = models.DateTimeField(null=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pk)
        super(Question, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    textLength = 32768
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    poster = models.ForeignKey(User,
                               on_delete=models.SET(get_sentinel_user))
    text = models.TextField(max_length=textLength)
    date = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.text

class Reply(models.Model):
    textLength = 32768
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    poster = models.ForeignKey(User,
                               on_delete=models.SET(get_sentinel_user))
    text = models.TextField(max_length=textLength)
    date = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = 'Replies'
    
    def __str__(self):
        return self.text

class Followed(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name + " followed by " + self.poster.username

class UpvoteQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # If upvoted, positive is true, otherwise is false
    positive = models.BooleanField(default=True)

    def __str__(self):
        if (positive):
            return self.question.title + " upvoted by " + self.user.username
        else:
            return self.question.title + " downvoted by " + self.user.username

class UpvoteAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # If upvoted, positive is true, otherwise is false
    positive = models.BooleanField(default=True)

    def __str__(self):
        if (positive):
            return "Answer upvoted by " + self.user.username
        else:
            return "Answer downvoted by " + self.user.username

class UpvoteReply(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # If upvoted, positive is true, otherwise is false
    positive = models.BooleanField(default=True)

    def __str__(self):
        if (positive):
            return "Reply upvoted by " + self.user.username
        else:
            return "Reply downvoted by " + self.user.username
