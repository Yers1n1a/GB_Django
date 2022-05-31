from pathlib import Path
from time import time
from django.db import models
from django.contrib.auth.models import AbstractUser
from mainap.models import NULLALLABLE


def users_avatars_path(instance, filename):
# file will be uploaded to
# MEDIA_ROOT / user_<username> / avatars / <filename>
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return f"user_{0}/avatars/{1}".format(instance.username, f"pic_{num}{suff}")


class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name='Email', unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', **NULLALLABLE)
    avatar = models.ImageField(upload_to=users_avatars_path, **NULLALLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'