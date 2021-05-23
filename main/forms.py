from django import forms

from main.models import Search


class InputForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'
