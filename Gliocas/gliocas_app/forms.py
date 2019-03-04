from django import forms
from gliocas_app.models import Question
from django.utils import timezone


class QuestionForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):

		self.user = kwargs.pop('user', None)
		self.course = kwargs.pop('course', None)

		super(QuestionForm, self).__init__(*args, **kwargs)

		self.fields['course'].initial = self.course
		self.fields['poster'].initial = self.user

	titleLength = 64
	textLength = 32768

	title = forms.CharField(max_length=titleLength, help_text="Please enter how you'd like to title your question.")
	text = forms.CharField(max_length=textLength, help_text="Please enter the text of your question.")
	course = forms.CharField(widget=forms.HiddenInput())
	poster = forms.CharField(widget=forms.HiddenInput())
	date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	upvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Question
		fields = ('course', 'title', 'text', 'poster', 'date', 'views', 'slug')
