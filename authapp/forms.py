from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
import random, hashlib

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


class DebiUserCreationForm(AgeValidatorMixIn, UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'age',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for prompt, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {prompt}'
            field.help_text = ''

    def save(self):
        user = super().save()
        print(f'from forms.save(): {user}')
        user.is_active = False
        salt = hashlib.sha256(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha256(str(user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user

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
