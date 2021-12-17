# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from authapp.models import DebiUser


class DebiUserLoginFrom(AuthenticationForm):
    # class Meta:
    #     # model = DebiUser
    #     model = get_user_model()
    #     fields = (username, password)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for prompt, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {prompt}'
