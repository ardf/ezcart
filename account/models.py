from django.db import models
import uuid
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('Email address is required')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.name = name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(name,email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
        
class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    name = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    objects = UserManager()

    def __str__(self):
        return self.email
