from django import forms
from .models import Run
from crispy_forms.helper import FormHelper

class DateInput(forms.DateInput):
    input_type = 'date'

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ('activity','name', 'date', 'distance', 'duration')
        widgets = {
                'date': DateInput()
            }
    helper = FormHelper()
