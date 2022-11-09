# Generated by Django 4.1.2 on 2022-10-30 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_alter_usermood_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermood",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
