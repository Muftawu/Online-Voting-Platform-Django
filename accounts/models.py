from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password

class survote_user_Manager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        username = survote_user.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("user_type", 2)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", 1)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(username, email, password, **extra_fields)



class survote_user(AbstractUser):
    USER_TYPE = ((1, 'ADMIN'), (2, 'VOTER'))
    GENDER =(('Male', 'Male'), ('Female', 'Female'))

    username = models.CharField(max_length=150, null=True, blank=True, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    user_type = models.CharField(max_length=1, default=2, choices=USER_TYPE)
    gender = models.CharField(max_length=6, default=None, choices=GENDER, null=True, blank=True)
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    objects = survote_user_Manager()

    def __str__(self):
        return self.username