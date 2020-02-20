from django import forms

from core.models import *

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = [ 'id', 'text', 'member' ]


