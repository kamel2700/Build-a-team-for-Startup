from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import UserProfile, ProjectPage, Comment


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = None

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'image',
            'speciality',
            'description'
        )


class SectionExtractionForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'user': 'user'}),
                                           queryset=User.objects.all())

    class Meta:
        model = ProjectPage
        fields = '__all__'


class AddToProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectPage
        fields = (
            'title',
        )

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = ProjectPage
        fields = (
            'title',
            'type',
            'description',
        )

    def save(self, commit=True):
        project = super(ProjectCreateForm, self).save(commit=False)
        project.owner = self.owner
        project.title = self.cleaned_data['title']
        project.type = self.cleaned_data['type']
        project.description = self.cleaned_data['description']

        if commit:
            project.save()

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        super(ProjectCreateForm, self).__init__(*args, **kwargs)


class EditProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectPage
        fields = (
            'title',
            'type',
            'description',
            'image'
        )


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'text',
        )
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        comment = super(AddCommentForm, self).save(commit=False)
        comment.author = self.author
        comment.text = self.cleaned_data['text']

        comment.project = self.project
        comment.user_profile = self.user_profile

        if commit:
            comment.save()

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.project = kwargs.pop('project', None)
        self.user_profile = kwargs.pop('user_profile', None)
        super(AddCommentForm, self).__init__(*args, **kwargs)
