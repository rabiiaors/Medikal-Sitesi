from django import forms


class SearchForms(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
