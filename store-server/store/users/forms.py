from django.contrib.auth.forms import  AuthenticationForm

from users.models import User

class UserLoginForum(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')