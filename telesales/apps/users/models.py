import os
import jwt
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_active=True, is_admin=False):
        user = self.model(username=username, email=self.normalize_email(
            email), active=is_active, admin=is_admin)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password, is_admin=True)
        return user


class User(AbstractBaseUser):
    username = models.CharField(
        db_index=True, max_length=255, unique=True, default="new user")
    email = models.EmailField(db_index=True, max_length=255, unique=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        token = jwt.encode({
            'id': self.pk,
            'is_admin': self.admin,
            'exp': datetime.utcnow()+timedelta(days=60)
        }, os.environ.get('TELESALES_SECRET_KEY'), algorithm='HS256')
        return token.decode('utf-8')
