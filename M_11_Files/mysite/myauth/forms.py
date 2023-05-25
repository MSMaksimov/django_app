from django import forms
from myauth.models import Profile


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        if avatar:
            if avatar.size > 1024 * 1024:
                raise forms.ValidationError('File size too large (maximum is 1MB).')
        return avatar

