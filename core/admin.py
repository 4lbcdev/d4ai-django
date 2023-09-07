from django.contrib import admin
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import *

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    """
    User creation form instance
    """
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[RegexValidator(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', 
            _(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character (!@#$%).")
        )]
    )

    class Meta():
        model = User
        fields = ('email', 'alias', 'password1', 'password2', 'full_name', 'is_active', 'is_admin', 'is_staff')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    Changes a user instance field
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'alias', 'password', 'is_active', 'is_admin', 'is_staff')


class UserAdmin(BaseUserAdmin):
    """
    Defines the User admin view
    """
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'alias', 'date_joined','last_login', 'is_superuser', 'is_active', 'is_admin', 'is_staff')
    list_filter = ('is_admin', 'is_staff' )
    search_fields = ('email', 'alias',)
    readonly_fields = ('uid', 'date_joined','last_login')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        ('Personal info', {'fields': ('uid','email', 'alias','full_name')}),
        ('Meta', {'fields': ('date_joined','last_login')}),
        # ('Private', {'fields': ('password',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff', 'is_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'alias', 'password1', 'password2'),
        }),
    )


# Registers the new UserAdmin...
admin.site.register(User, UserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name', 'location')
admin.site.register(Event, EventAdmin)

class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name')
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

class ArticleTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name')
admin.site.register(ArticleTag, ArticleTagAdmin)

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
    list_display = ('id', 'title', 'category', 'publishdate', 'status')
admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent','content','timestamp')
    # readonly_fields = ('user', 'content', 'timestamp')
admin.site.register(Comment, CommentAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id','date','email')
    readonly_fields = ('date','first_name','last_name','email')
admin.site.register(Subscriber, SubscriberAdmin)

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','email','area_of_interest')
    readonly_fields = ('full_name','email','area_of_interest')
admin.site.register(Volunteer, VolunteerAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','email','message')
    readonly_fields = ('full_name','email','message')
admin.site.register(Contact, ContactAdmin)
