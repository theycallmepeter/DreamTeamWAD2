from django import forms
from rango.models import Question


class QuestionForm(forms.ModelForm):

	titleLength = 64
    textLength = 32768

	def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.questions = kwargs.pop('questions', None)
        super(QuestionForm, self).__init__(*args, **kwargs)

    course = forms.ChoiceField(choices=questions, help_text="Choose the course to which your question is related.")
    title = forms.CharField(max_length=titleLength, help_text="Please enter how you'd like to title your question.")
    text = forms.CharField(max_length=textLength, help_text="Please enter the text of your question.")
	poster = forms.CharField(widget=forms.HiddenInput(), initial=self.user.username)
    date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    upvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Question
        fields = ('course', 'title', 'text')
