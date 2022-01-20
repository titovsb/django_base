# Generated by Django 3.2.9 on 2022-01-18 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0005_alter_debiuser_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="DebiUserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tagline",
                    models.CharField(blank=True, max_length=128, verbose_name="тэги"),
                ),
                (
                    "about",
                    models.TextField(blank=True, max_length=256, verbose_name="о себе"),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("M", "Мужчина"),
                            ("F", "Женщина"),
                            ("X", "Неопределившийся"),
                            ("A", "Инопланетянин"),
                        ],
                        max_length=1,
                        verbose_name="пол",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
