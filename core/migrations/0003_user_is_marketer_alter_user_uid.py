# Generated by Django 4.2.3 on 2023-10-12 08:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_marketer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('0faedbe7-a1a3-440f-9705-a32761100d27'), primary_key=True, serialize=False),
        ),
    ]