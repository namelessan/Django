from django import forms
from .models import Shout

class AddShout(forms.ModelForm):
    class Meta:
        model = Shout
        fields = ('shout_text',)
