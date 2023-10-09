from django import forms
from .models import Post, TextEntry

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class TextEntryForm(forms.Form):
    text_to_translate = forms.CharField(widget=forms.Textarea(attrs={ 'style': 'height: 6em;'}))