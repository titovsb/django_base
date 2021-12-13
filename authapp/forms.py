from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

# from authapp.models import DebiUser


class DebiUserLoginFrom(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for prompt, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {prompt}'


class DebiUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'age', 'avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for prompt, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {prompt}'
            field.help_text = ''


class DebiUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'age', 'avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for prompt, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {prompt}'
