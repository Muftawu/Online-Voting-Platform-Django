from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import survote_user

class survote_user_form(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Username 
        self.fields["username"].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'Username...',
            'minlength': '3',
            'maxlength': '20',
        })

        # Email  
        self.fields["email"].widget.attrs.update({
            'class': 'form-control',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'example@gmail.com...',
        })

        # Password1 
        self.fields["password1"].widget.attrs.update({
            'class': 'form-control',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': 'Password...',
            'minlength': '5',
            'maxlength': '20',
        })

        # Password2 
        self.fields["password2"].widget.attrs.update({
            'class': 'form-control',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': 'Password...',
            'minlength': '5',
            'maxlength': '20',
        })
    class Meta:
        model = survote_user
        fields = ["username", "email", "password1", "password2"]
