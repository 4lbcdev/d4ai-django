# from core.models import Volunteers, Subscribers
# from django import forms
# from ckeditor.widgets import CKEditorWidget


# class contactForm(forms.ModelForm):
#     parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
#     content = forms.CharField(
#         widget=forms.Textarea(attrs={
#             'rows':4, 
#             'placeholder': 'This conversation is moderated.'
#         }), 
#         min_length=1, 
#         max_length=420
#     )


# class subscribeForm(forms.ModelForm):
#     email = forms.EmailField ()

#     class Meta:
#         model = Mailing
#         fields = ['email',]


# class volunteerForm(forms.ModelForm):
#     content = forms.CharField (min_length=1, max_length=500)
#     ratings = forms.RadioSelect()

#     class Meta:
#         model = Feedback
#         fields = ['content', 'ratings',]
