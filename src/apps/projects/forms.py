from django.core.validators import RegexValidator, MinLengthValidator
from django import forms
from django_countries.fields import CountryField

from .models import Project


class ProjectFormScreen1(forms.Form):
    title = forms.CharField(
        max_length=120,
        validators=[MinLengthValidator(6)],
        widget=forms.TextInput(attrs={
            'class': 'profile-textinput input TextmdRegular',
        })
    )
    subtitle = forms.CharField(widget=forms.Textarea)

    description = forms.CharField(widget=forms.Textarea)

    location = CountryField().formfield(
        required=False,
        widget=forms.Select(attrs={
            'class': 'profile-select input'
        })
    )


class ProjectFormScreen2(forms.Form):
    loan_amount = forms.IntegerField()
    repayment_period = forms.IntegerField()


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'subtitle', 'description',
                  'location', 'loan_amount', 'repayment_period']
