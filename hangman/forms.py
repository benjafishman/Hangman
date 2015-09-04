__author__ = 'benfishman'

from django import forms

from django.core import validators

import re


class GuessLetterForm(forms.Form):
    letter = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Guess'}),
                             label_suffix='',
                             label='',
                             max_length=100,
                            )


    def clean_letter(self):
        letter = self.cleaned_data['letter']
        pattern = re.compile("^([a-zA-Z]+)$")
        if pattern.search(letter):
            return letter.lower()
        else:
            raise forms.ValidationError('input must be valid word or letter')




