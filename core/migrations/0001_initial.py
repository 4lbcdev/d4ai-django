# Generated by Django 4.2.3 on 2023-08-03 10:09

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('uid', models.UUIDField(default=uuid.UUID('ef9cbe59-2abd-4354-a65c-fc99c65730dc'), primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('alias', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_]{3,18}$', message="Username should be between 3-18 characters, and must contain letters, numbers, or '_' only.")], verbose_name='Username')),
                ('full_name', models.CharField(default='No name', max_length=255, null=True, verbose_name='Full name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'article_category',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'article_tag',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(default='No name', max_length=255, null=True, verbose_name='Full name')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='events/')),
                ('posterURI', models.URLField()),
                ('url', models.URLField()),
            ],
            options={
                'db_table': 'event',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, default='No first name', max_length=255, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, default='No last name', max_length=255, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
            options={
                'db_table': 'subscribers',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(default='No name', max_length=255, null=True, verbose_name='Full name')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('area_of_interest', models.CharField(blank=True, max_length=250, null=True)),
                ('about_me', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'volunteers',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content', models.TextField(max_length=420)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_flagged', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('featureimage', models.ImageField(upload_to='articles/')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=500)),
                ('writer', models.CharField(default='D4AI Team', max_length=100)),
                ('publishdate', models.DateField()),
                ('extract', models.CharField(blank=True, max_length=2000, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Publish')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='core.articlecategory')),
                ('tags', models.ManyToManyField(related_name='tags', to='core.articletag')),
            ],
            options={
                'db_table': 'article',
                'ordering': ['-publishdate'],
            },
        ),
    ]
