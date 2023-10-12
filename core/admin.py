from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AdminPasswordChangeForm
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import *
from functools import wraps
from django.http import HttpResponseForbidden

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    """ User creation form instance
    """
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[RegexValidator(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', 
            _(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character (!@#$%).")
        )]
    )

    class Meta:
        model = User
        fields = ('email', 'alias', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        # user.set_password(self.cleaned_data["password"])
        user.password = make_password("default123@d4ai")
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """ Changes a user instance field
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'alias', 'password', 'is_active', 'is_admin', 'is_staff', 'is_marketer')


class UserAdmin(admin.ModelAdmin):
    """ Defines the User admin view
    """
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'alias', 'date_joined','last_login', 'is_active')
    list_filter = ('is_active','is_staff')
    search_fields = ('email', 'alias',)
    readonly_fields = ('uid', 'date_joined','last_login')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        ('Personal info', {'fields': ('uid','email', 'alias','full_name')}),
        # ('Meta', {'fields': ('date_joined','last_login')}),
        ('Private', {'fields': ('password',)}),
        ('Role', {'fields': ('is_admin', 'is_marketer')}),
    )
    # Add a change password form to the user change view.
    change_password_form = AdminPasswordChangeForm

    def save_model(self, request, obj, form, change):
        """
        Set the default password when creating a new user through the admin interface.
        """
        if not change:
            # Only set the default password when creating a new user, not when editing an existing one.
            obj.password = make_password("default123@d4ai")  # Set the hashed default password
        super().save_model(request, obj, form, change)


class EventAdmin(admin.ModelAdmin):
    """ Admin class for Event
    """
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name', 'location')


class ArticleCategoryAdmin(admin.ModelAdmin):
    """ Admin class for ArticleCategory
    """
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name')

    def has_add_permission(self, request):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_save_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False


class ArticleTagAdmin(admin.ModelAdmin):
    """ Admin class for ArticleTag
    """
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name')

    def has_add_permission(self, request):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_save_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False


class ArticleAdmin(admin.ModelAdmin):
    """ Admin class for Article
    """
    prepopulated_fields = {'slug': ('title',),}
    list_display = ('id', 'title', 'category', 'publishdate', 'status')

    def has_add_permission(self, request):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_save_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False


class CommentAdmin(admin.ModelAdmin):
    """ Admin class for Comment
    """
    list_display = ('id', 'parent','content','timestamp')
    # readonly_fields = ('user', 'content', 'timestamp')

    def has_add_permission(self, request):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser:
            return True
        return False

    def has_save_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser:
            return True
        return False    


class SubscriberAdmin(admin.ModelAdmin):
    """ Admin class for subscriber
    """
    list_display = ('id','date','email')
    readonly_fields = ('date','first_name','last_name','email')

    def has_add_permission(self, request):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_save_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser or request.user.is_marketer:
            return True
        return False


class VolunteerAdmin(admin.ModelAdmin):
    """ Admin class for Volunteer
    """
    list_display = ('id','full_name','email','area_of_interest')
    readonly_fields = ('full_name','email','area_of_interest')


class ContactAdmin(admin.ModelAdmin):
    """ Admin class for Contact
    """
    list_display = ('id','full_name','email','message')
    readonly_fields = ('full_name','email','message')


# Registers the new UserAdmin...
admin.site.register(User, UserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Contact, ContactAdmin)
