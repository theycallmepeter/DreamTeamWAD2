from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

def get_sentinel_user():
    return User.objects.get_or_create(username='Deleted',
                                      email='obiwan@kenobi.com',
                                      password='High ground')[0]

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
    titleLength = 64
    textLength = 32768
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    poster = models.ForeignKey(User,
                               on_delete=models.SET(get_sentinel_user))
    title = models.CharField(max_length=titleLength)
    text = models.TextField(max_length=textLength)
    date = models.DateTimeField()
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pk)
        super(Question, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Answer(models.Model):
    textLength = 32768
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    poster = models.ForeignKey(User,
                               on_delete=models.SET(get_sentinel_user))
    text = models.TextField(max_length=textLength)
    date = models.DateTimeField()
    upvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Reply(models.Model):
    textLength = 32768
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    poster = models.ForeignKey(User,
                               on_delete=models.SET(get_sentinel_user))
    text = models.TextField(max_length=textLength)
    date = models.DateTimeField()
    upvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Followed(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
