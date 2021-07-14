from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['email',
                  'username', 'first_name', 'password1', 'password2', ]
        label = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'email', 'username',
            'location', 'bio', 'short_intro',
            'profile_image', 'social_github',
            'social_twiter', 'social_youtube',
            'social_website',
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})
