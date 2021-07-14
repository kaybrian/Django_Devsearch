from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    class meta:
        model = User
        fields = '__all__'
        label = {
            'first_name': 'Name',
        }
