from django import forms
from .models import CSS

class CSSForm(forms,ModelForm):
    class Meta:
        model = CSS
        field = ['title', 'area', 'time', 'mood', 'floor','toilet',
        'smoke','elevator','pet','add']