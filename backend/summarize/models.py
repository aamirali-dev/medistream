from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserAccountManager(BaseUserManager):
    """
    Custom manager for the UserAccount model.
    """
    def create_user(self, email, username, password=None, **extra_fields):
        """
               Creates and saves a new user with the given email, username, and password.

               Args:
                   email (str): The user's email address.
                   username (str): The user's username.
                   password (str): The user's password.
                   **extra_fields: Additional fields to be saved in the user's profile.

               Returns:
                   UserAccount: The newly created user account.

               Raises:
                   ValueError: If email is not provided.
               """
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
               Creates and saves a new superuser with the given username, email, and password.

               Args:
                   username (str): The superuser's username.
                   email (str): The superuser's email address.
                   password (str): The superuser's password.
                   **extra_fields: Additional fields to be saved in the superuser's profile.

               Returns:
                   UserAccount: The newly created superuser account.
               """
        user = self.create_user(username, email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """
    Custom UserAccount model.
    """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def get_full_name(self):
        """
        Returns the user's full name.

        Returns:
            str: The user's full name in the format "first_name - last_name".
        """
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        """
        Returns the user's short name.

        Returns:
            str: The user's username.
        """
        return self.username

    def __str__(self):
        """
        Returns a string representation of the user account.

        Returns:
            str: The user's email address.
        """
        return self.email


class Prompts(models.Model):
    """
    Prompts model to store history of prompts issued by the user.
    """

    user = models.ForeignKey(UserAccount, on_delete=models.PROTECT, related_name='prompts')
    prompt = models.TextField()
    patient_id = models.IntegerField(default=7273)
    date = models.DateField(default = None)
    date_created = models.DateTimeField(auto_now_add=True)