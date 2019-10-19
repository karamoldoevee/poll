from django import forms

from webapp.models import Poll, Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_at']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = []

class PollChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']