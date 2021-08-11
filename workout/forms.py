from django import forms
from .models import Run
class DateInput(forms.DateInput):
    input_type = 'date'

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ('activity','name', 'date', 'distance', 'duration')
        widgets = {
                'date': DateInput()
            }
