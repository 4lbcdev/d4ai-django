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


def staff_member_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_staff or request.user.is_admin or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return _wrapped_view


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
    """
    Changes a user instance field
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'alias', 'password', 'is_active', 'is_admin', 'is_staff')


class UserAdmin(admin.ModelAdmin):
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
        ('Private', {'fields': ('password',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff', 'is_admin')}),
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


# Registers the new UserAdmin...
admin.site.register(User, UserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


# Admin for Event
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name', 'location')


admin.site.register(Event, EventAdmin)


# Admin for ArticleCategory
class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name')

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


admin.site.register(ArticleCategory, ArticleCategoryAdmin)


# Admin for ArticleTag
class ArticleTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name')

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


admin.site.register(ArticleTag, ArticleTagAdmin)


# Admin for Article
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
    list_display = ('id', 'title', 'category', 'publishdate', 'status')

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


admin.site.register(Article, ArticleAdmin)


# Admin for Comment
class CommentAdmin(admin.ModelAdmin):
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

    
admin.site.register(Comment, CommentAdmin)


# Admin for Subscriber
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id','date','email')
    readonly_fields = ('date','first_name','last_name','email')


admin.site.register(Subscriber, SubscriberAdmin)


# Admin for Volunteer
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','email','area_of_interest')
    readonly_fields = ('full_name','email','area_of_interest')


admin.site.register(Volunteer, VolunteerAdmin)


# Admin for Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','email','message')
    readonly_fields = ('full_name','email','message')


admin.site.register(Contact, ContactAdmin)
