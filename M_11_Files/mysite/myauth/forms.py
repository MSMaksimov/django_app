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
            # if avatar.content_type not in ['image/jpeg', 'image/png']:
            #     raise forms.ValidationError('Invalid file type (only JPEG and PNG are accepted).')
        return avatar

