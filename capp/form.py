from django import forms
from .models import CSS, Comment

class CSSForm(forms.ModelForm):
    class Meta:
        model = CSS
        fields = ['title', 'area', 'time', 'mood', 'floor','toilet',
        'smoke','elevator','pet','add', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writer', 'text',)