# Generated by Django 4.1.7 on 2024-08-21 11:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_is_staff_alter_user_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IPAddres', models.GenericIPAddressField(default='0.0.0.0')),
                ('page', models.CharField(max_length=40, null=True)),
                ('device', models.CharField(default='null', max_length=400)),
                ('visited', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'stats',
                'ordering': ['-page'],
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a337a4fd-8901-44ca-9f56-1c8f10117841'), primary_key=True, serialize=False),
        ),
    ]