from django import forms
from gliocas_app.models import Question, Course
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):

		self.user = kwargs.pop('user', None)
		# self.course = kwargs.pop('course', None)

		super(QuestionForm, self).__init__(*args, **kwargs)
		# self.fields['course'].initial = course_obj.slug
		self.fields['poster'].initial = 'rango'
		# self.fields['poster'].initial = self.user.get_username()

	titleLength = 64
	textLength = 32768

	title = forms.CharField(max_length=titleLength, help_text="Please enter how you'd like to title your question.", required = True)
	text = forms.CharField(widget=forms.Textarea, max_length=textLength, help_text="Please enter the text of your question.", required = True)
	# course = forms.CharField(widget=forms.HiddenInput())
	poster = forms.CharField(widget=forms.HiddenInput())
	date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	# upvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	# slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Question
		fields = ('title', 'text', 'date', 'views',) #'slug')

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
