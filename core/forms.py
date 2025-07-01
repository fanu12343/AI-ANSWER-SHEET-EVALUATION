from django import forms
from .models import Question, StudentAnswer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['teacher', 'text','ideal_answer']

class AnswerUploadForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = ['question', 'student_name', 'answer_image']
