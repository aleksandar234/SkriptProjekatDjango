from django import forms

class SnippetForm(forms.Form):
    question = forms.CharField(max_length=100)
    choice1 = forms.CharField(max_length=100)
    choice2 = forms.CharField(max_length=100)
    choice3 = forms.CharField(max_length=100)
