from django import forms
from gliocas_app.models import Question, Course
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):

    titleLength = 256
    textLength = 32768

    title = forms.CharField(max_length=titleLength, help_text="Please enter how you'd like to title your question.", required = True)
    text = forms.CharField(widget=forms.Textarea, max_length=textLength, help_text="Please enter the text of your question.", required = True)
    date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Question
        fields = ('title', 'text', 'date', 'views',)

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class CourseForm(forms.ModelForm):
    maxLength = 64
    textLength = 32768

    name = forms.CharField(max_length=maxLength, help_text="Please enter the short name of your course (e.g. 2A)", required = True)

    class Meta:
        model = Course
        fields = ('name',)


