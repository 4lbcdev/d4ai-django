"""models module: handles a user class
"""
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.deletion import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import uuid


class UserManager(BaseUserManager):
    """
    saves a User instance as either a normal user with or without superuser previledges
    """

    def create_user(self, email, password=None):
        """
        class method that creates a normal user
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model( email=self.normalize_email(email))
        # user.set_password(password)
        user.set_password("default1234")
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """
        class method that creates a superuser
        """
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    defines a User instance
    """
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    email = models.EmailField(verbose_name=_('Email'), max_length=100, unique=True)
    alias = models.CharField(verbose_name=_('Username'), max_length=18, unique=True,
        validators=[RegexValidator(r'^[a-zA-Z0-9_]{3,18}$', message="Username should be between 3-18 characters, and must contain letters, numbers, or '_' only.")]
        )
    # password = models.CharField(
    #     verbose_name=_('Password'),
    #     max_length=24,
    #     validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', message=_(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character."))]
    # )
    full_name = models.CharField(verbose_name=_('Full name'), max_length=255, null=True, blank=False, default="No name")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['alias',]

    def __str__(self):
        """
        Returns a strings representation of a user instance
        """
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Returns admin status of a user instance
        """
        return self.is_admin
        
    def has_module_perms(self, app_label):
        """
        Returns user instance permissions
        """
        return True


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    name = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length = 500)
    location = models.CharField(max_length=100, blank=False)
    poster = models.ImageField(upload_to='events/')
    posterURI = models.URLField()
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
        db_table = 'event'


class ArticleCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'article_category'

class ArticleTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length = 500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'article_tag'


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    featureimage = models.ImageField(upload_to='articles/')
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    tags = models.ManyToManyField(ArticleTag, related_name='tags')
    category = models.ForeignKey(ArticleCategory, related_name='articles', on_delete=models.PROTECT)
    writer = models.CharField(max_length=100, default = 'D4AI Team')
    publishdate = models.DateField(auto_now_add=False)
    extract = models.CharField(max_length=2000, blank=True, null=True)
    content = RichTextField(config_name='full_editor', blank=True, null=True)
    POST_STATUS = (
        ('D', 'Draft'),
        ('P', 'Publish'),
    )
    status = models.CharField(max_length=10, choices=POST_STATUS)

    def get_absolute_url(self):
        return f'/blog/{self.id}/{self.slug}/'

    @property
    def url(self):
        return f'/blog/{self.id}/{self.slug}/'

    @property
    def viewCount(self):
        return ArticleStat.objects.filter(article=self).count()

    @property
    def comments(self):
        qs = Comment.objects.filter_by_instance(self)
        return qs
    
    @property
    def commentCount(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        qs = Comment.objects.filter(content_type=content_type, object_id=self.id).count()
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishdate']
        db_table = 'article'


class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
        return qs


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=420, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_flagged = models.BooleanField(default=False)

    objects = CommentManager()
    
    def replies(self):
        return Comment.objects.filter(parent=self).order_by('timestamp')

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    class Meta:
        ordering = ['-timestamp']
        db_table = 'comments'


class Subscriber(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(verbose_name=_('First name'), max_length=255, null=True, blank=True, default="No first name")
    last_name = models.CharField(verbose_name=_('Last name'), max_length=255, null=True, blank=True, default="No last name")
    email = models.EmailField(verbose_name=_('Email'), max_length=100)

    class Meta:
        db_table = 'subscribers'


class Volunteer(models.Model):
    """
    Defines an volunteer instance
    """
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(verbose_name=_('Full name'), max_length=255, null=True, blank=False, default="No name")
    email = models.EmailField(verbose_name=_('Email'), max_length=100, unique=True)
    area_of_interest = models.CharField(max_length=250, blank=True, null=True)
    about_me = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'volunteers'


class Contact(models.Model):
    """
    Defines a contact instance
    """
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(verbose_name=_('Full name'), max_length=255, null=True, blank=False, default="No name")
    email = models.EmailField(verbose_name=_('Email'), max_length=100, unique=True)
    message = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'contact'
