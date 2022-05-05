import uuid

from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from config.utils.models import Entity


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

    def create_user(self, first_name, last_name, email, password=None,address=None,birthdate=None,gender=None,bloodType=None,phoneNumber=None):
        if not email:
            raise ValueError('user must have email')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.address=address
        user.bloodType=bloodType
        user.birthdate=birthdate
        user.gender=gender
        user.phoneNumber=phoneNumber
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('user must have email')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser, Entity):

    username = models.NOT_PROVIDED
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField("first_name", max_length=50)
    last_name = models.CharField("last_name", max_length=50)
    password = models.CharField(_('password'), max_length=128)
    birthdate = models.DateField(max_length=25, null=True, blank=True)
    bloodType = models.CharField(max_length=3, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    phoneNumber = models.IntegerField( null=True, blank=True)

    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True