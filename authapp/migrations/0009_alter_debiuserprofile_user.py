# Generated by Django 3.2.9 on 2022-02-09 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0008_alter_debiuserprofile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="debiuserprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
