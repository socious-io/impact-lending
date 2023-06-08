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
    subtitle = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'textarea TextmdRegular',
        'rows': '3'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'textarea TextmdRegular',
        'rows': '5'
    }))

    video_link = forms.URLField(required=False, widget=forms.TextInput(attrs={
        'class': 'profile-textinput input TextmdRegular',
    }))

    location = CountryField().formfield(
        required=False,
        widget=forms.Select(attrs={
            'class': 'profile-select input'
        })
    )


class ProjectFormScreen2(forms.Form):
    REPAYMENT_CHOICES = [(i*6, f'{i*6} months') for i in range(1, 5)]
    loan_amount = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': "create-project-step2-textinput TextmdRegular",
        'placeholder': '1000'
    }))
    repayment_period = forms.ChoiceField(choices=REPAYMENT_CHOICES, widget=forms.Select(attrs={
        'class': 'input'
    }))


class ProjectFormScreen3(forms.Form):
    transaction_id = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'hide',
        'id': 'project-transaction-id'
    }))


class ImageForm(forms.Form):
    photo = forms.ImageField(required=True)
