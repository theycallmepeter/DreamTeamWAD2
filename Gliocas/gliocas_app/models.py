from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    def __str__(self):
        return self.user.username

class Subject(models.Model):
    maxLength = 64
    name = models.CharField(max_length=maxLength, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    maxLength = 64
    name = models.CharField(max_length=maxLength, unique=True)
    subject = models.ForeignKey(Subject)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    titleLength = 64
    textLength = 32768
    course = models.ForeignKey(Course)
    poster = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=titleLength)
    text = models.TextField(max_length=textLength)
    date = models.DatetimeField()
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Answer(models.Model):
    textLength = 32768
    question = models.ForeignKey(Question)
    poster = models.ForeignKey(UserProfile)
    text = models.TextField(max_length=textLength)
    date = models.DatetimeField()
    upvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Reply(models.Model):
    textLength = 32768
    answer = models.ForeignKey(Answer)
    poster = models.ForeignKey(UserProfile)
    text = models.TextField(max_length=textLength)
    date = models.DatetimeField()
    upvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Followed(models.Model):
    course = models.ForeignKey(Course)
    poster = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.name
