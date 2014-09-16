from django import forms


class Song_form(forms.Form):
    #answer = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 4}))
     answer = forms.CharField(widget=forms.TextInput())