from django import forms

from mainapp.models import ProductCategory, Product
from authapp.models import DebiUser, DebiUserProfile

from authapp.forms import (
    DebiUserProfileEditForm,
    DebiUserChangeForm,
    USER_FIELDS,
    PROFILE_FIELDS,
)


class AdminDebiUserEditForm(DebiUserChangeForm):
    class Meta:
        model = DebiUser
        # fields = '__all__'    # все поля нам не требуются
        fields = USER_FIELDS


class AdminDebiUserProfileEditForm(DebiUserProfileEditForm):
    class Meta:
        model = DebiUserProfile
        fields = PROFILE_FIELDS


class AdminProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""


class AdminProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""
