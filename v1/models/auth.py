from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models


def user_type(key):
    return {
        "direktor": 1,
        "ombor": 2,
        "magazin": 3
    }.get(key, 0)


class CostumUserManager(UserManager):
    def create_user(self, phone, password=None, is_staff=False, is_superuser=False, is_active=True, **extra_fields):
        user = self.model(
            phone=phone,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        return self.create_user(phone=phone, password=password, is_staff=True, is_superuser=True, is_active=True,
                                **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    lastname = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    usertype = models.SmallIntegerField(default=0)

    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = CostumUserManager()

    USERNAME_FIELD = 'phone'

class OTP(models.Model):
    email = models.EmailField()
    key = models.CharField(max_length=150)

    is_conf = models.BooleanField(default=False)
    is_expire = models.BooleanField(default=False)
    tries = models.BooleanField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.tries >= 3:
            self.is_expire = True
            super(OTP, self).save(*args, **kwargs)
