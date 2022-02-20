import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta

from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver


def get_expiration_date():
    return timezone.now() + timedelta(hours=24)


class DebiUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(verbose_name="возраст", null=True, default=18)
    activation_key = models.CharField(
        verbose_name="ключ активации", max_length=64, null=True
    )
    expiration_date = models.DateTimeField(
        verbose_name="код активации истекает", default=get_expiration_date
    )
    is_active = models.BooleanField(verbose_name="активный/приостановлен", default=True)

    def is_activation_expired(self):
        if timezone.now() <= self.expiration_date:
            return False
        else:
            return True


class DebiUserProfile(models.Model):
    MALE, FEMALE, NONBINARY, ALIEN = "M", "F", "X", "A"
    GENDER_CHOICES = (
        (MALE, "Мужчина"),
        (FEMALE, "Женщина"),
        (NONBINARY, "Неопределившийся"),
        (ALIEN, "Инопланетянин"),
    )
    user = models.OneToOneField(
        DebiUser,
        null=False,
        db_index=True,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(verbose_name="аватарка", upload_to="avatars", blank=True)
    tagline = models.CharField(verbose_name="тэги", max_length=128, blank=True)
    about = models.TextField(verbose_name="о себе", max_length=256, blank=True)
    gender = models.CharField(
        verbose_name="пол", max_length=1, choices=GENDER_CHOICES, blank=True
    )

    # @receiver(post_save, sender=DebiUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            DebiUserProfile.objects.get_or_create(user=instance)
            # DebiUserProfile.objects.create(user=instance)
        else:
            instance.profile.save()


# перенесли код сохранения в предыдущую функцию
# @receiver(post_save, sender=DebiUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.debiuserprofile.save()
