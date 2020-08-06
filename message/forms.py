from django import forms
from .models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ""

        self.fields['content'].widget.attrs.update({
            'class':'note_form',
        })


