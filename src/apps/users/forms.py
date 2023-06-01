from django import forms
from django_countries.fields import CountryField
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from .models import User

alpha_num_validator = RegexValidator(
    r'^[a-zA-Z0-9]*$',
    'Only alphanumeric characters are allowed.',
)


class ProfileForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        validators=[alpha_num_validator, MinLengthValidator(6)],
        widget=forms.TextInput(attrs={
            'class': 'profile-textinput input TextmdRegular',
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=False,
        validators=[alpha_num_validator,],
        widget=forms.TextInput(attrs={
            'class': 'profile-textinput input TextmdRegular',
        })
    )
    first_name = forms.CharField(
        max_length=100,
        required=False,
        validators=[alpha_num_validator,],
        widget=forms.TextInput(attrs={
            'class': 'profile-textinput input TextmdRegular',
        })
    )
    country = CountryField().formfield(
        required=False,
        widget=forms.Select(attrs={
            'class': 'profile-select input'
        })
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        error = ValidationError('Username already taken')

        exclude = ('admin', 'socious', 'administrator')

        if username in exclude:
            raise error

        if User.objects.filter(username=username).exclude(id=self.request.user.id).exists():
            raise error

        return username
