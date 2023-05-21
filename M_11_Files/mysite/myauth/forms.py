from django.forms import ModelForm
from django import forms

from myauth.models import Profile


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "avatar",
