# Generated by Django 3.1.5 on 2021-03-03 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Token",
            fields=[
                ("key", models.CharField(max_length=70, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="token",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
