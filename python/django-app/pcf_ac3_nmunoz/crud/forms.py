# from .models import Usuario
# from .forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
"""
class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__' """

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
