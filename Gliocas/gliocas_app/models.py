from django.db import models
from django.template.defaultfilters import slugify

class Subject(models.Model):
    name = models.CharField(max_length=128,unique=True)
    slug = models.SlugField(unique=True)
    # other attributes

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject,self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=128, unique = True)
    subject = models.ForeignKey(Subject, models.PROTECT)
    slug = models.SlugField(unique = True)
    # other attributes

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course,self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Question(models.Model):
    subject = models.ForeignKey(Subject, models.PROTECT)
    course = models.ForeignKey(Course, models.PROTECT)
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    # other attributes

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question,self).save(*args, **kwargs)

    def __str__(self):
        return self.title