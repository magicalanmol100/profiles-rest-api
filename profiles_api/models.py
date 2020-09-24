from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserProfileManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames and manages the user profiles
    """
    def create_user(self, email, name,password=None):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('User must have an email address'))
        email = self.normalize_email(email)
        user = self.model(name=name,email=email)
        user.set_password(password)
        #So that password is stored as hash
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user=self.create_user(email, name, password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    def __str__(self):
        """Returns string representation of our user"""
        return self.email
