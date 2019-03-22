from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Function for setting the user attribute of questions, answers and replies to
# be an special account when a user account is deleted
def get_sentinel_user():
    user = User.objects.get_or_create(username='Deleted')[0]
    user.email = 'obiwan@kenobi.com'
    user.password = 'High ground'
    user.set_password(user.password)
    return user

# Subjects are things like MAthematics or Computing Science
class Subject(models.Model):
    maxLength = 64
    name = models.CharField(max_length=maxLength, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

# Courses are things like OOSE 2 or WAD 2
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
    picture = models.ImageField(upload_to='question_images', blank=True)
    slug = models.SlugField(max_length=8, default=get_random_string, unique=True)
    
    def __str__(self):
        return self.title

# Answer to questions
class Answer(models.Model):
    textLength = 32768
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    poster = models.ForeignKey(User,
                               on_delete=models.SET(get_sentinel_user))
    text = models.TextField(max_length=textLength)
    date = models.DateTimeField(null=True)
    picture = models.ImageField(upload_to='question_images', blank=True)
    
    def __str__(self):
        return self.text

# Reply to answers
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

# Model that represents a many-to-many relationship between user and course
# that consists on the user following the question
class Followed(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Followed courses'

    def __str__(self):
        return self.course.name + " followed by " + self.poster.username

# Model that represents a many-to-many relationship between user and question
# that consists on the user liking/disliking the question
class UpvoteQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # If upvoted, positive is true, otherwise is false
    positive = models.BooleanField(default=True)

    def __str__(self):
        if (self.positive):
            return self.question.title + " upvoted by " + self.user.username
        else:
            return self.question.title + " downvoted by " + self.user.username

# Model that represents a many-to-many relationship between user and answer
# that consists on the user liking/disliking the answer
class UpvoteAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # If upvoted, positive is true, otherwise is false
    positive = models.BooleanField(default=True)

    def __str__(self):
        if (self.positive):
            return "Answer with pk " + str(self.answer.pk) + " upvoted by " + self.user.username
        else:
            return "Answer with pk " + str(self.answer.pk) + " downvoted by " + self.user.username

# Model that represents a many-to-many relationship between user and reply
# that consists on the user liking/disliking the reply
class UpvoteReply(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # If upvoted, positive is true, otherwise is false
    positive = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Upvote replies'

    def __str__(self):
        if (self.positive):
            return "Reply with pk " + str(self.reply.pk) + " upvoted by " + self.user.username
        else:
            return "Reply with pk " + str(self.reply.pk) + " downvoted by " + self.user.username
