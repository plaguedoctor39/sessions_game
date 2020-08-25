from django import forms
from django.core.exceptions import ValidationError

from .models import PlayerGameInfo


class AnswerForm(forms.ModelForm):
    answer = forms.IntegerField(widget=forms.TextInput, label='Ответ')

    class Meta(object):
        model = PlayerGameInfo
        fields = ('answer', )
