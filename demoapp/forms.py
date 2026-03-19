from django import forms

SHIFTS = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Evening"),
)
class InputForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField()