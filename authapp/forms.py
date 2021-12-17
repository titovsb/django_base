from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

# from authapp.models import DebiUser
from django.forms import HiddenInput, forms


class DebiUserLoginFrom(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for prompt, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {prompt}'

class AgeValidatorMixIn:
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 18:
            raise forms.ValidationError('Вы слишком молоды')
        return age

class DebiUserCreationForm(AgeValidatorMixIn ,UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'age',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for prompt, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {prompt}'
            field.help_text = ''

class DebiUserChangeForm(AgeValidatorMixIn, UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'age', 'avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for prompt, field in self.fields.items():
            if prompt == 'password':
                field.widget = HiddenInput()
                continue
            field.widget.attrs['class'] = f'form-control {prompt}'
