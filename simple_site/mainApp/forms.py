from django import forms

class DateTime(forms.Form):
    date = forms.DateField(initial='23/12/2016')
    time = forms.TimeField(initial='14:34')