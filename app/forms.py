from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from app.models import *
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(
        widget=forms.PasswordInput(), required=True)

    def clean_username(self):
        data_username = self.cleaned_data['username']

        if not User.objects.filter(username=data_username).exists():
            raise forms.ValidationError("Wrong username")

        return data_username

    def clean_password(self):
        data_username = self.data['username']
        data_password = self.cleaned_data['password']

        if User.objects.filter(username=data_username).exists() and not authenticate(username=data_username,
                                                                                     password=data_password):
            raise forms.ValidationError("Wrong password")

        return data_password


class SignUpForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(
        widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean_username(self):
        data_username = self.cleaned_data['username']
        # if User.objects.filter(username=data_username).exists():
        #    raise forms.ValidationError("Wrong username")
        return data_username

    def clean_password(self):
        # data_username = self.cleaned_data['username']
        data_password = self.cleaned_data['password']

        if len(data_password) < 8:
            raise ValidationError("Password must contain at least 8 symbols")

        #                           password=data_password).exists():
        #    raise forms.ValidationError("Wrong password")

        return data_password


class EditProfile(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(max_length=50)

    # avatar = forms.ImageField()

    class Meta:
        model = Profile
        fields = ["username", "email", "avatar"]

    def clean_username(self):
        data_username = self.cleaned_data['username']
        return data_username

    def clean_avatar(self):
        data_avatar = self.cleaned_data['avatar']
        return data_avatar


class AddQuestion(forms.ModelForm):
    title = forms.CharField(label='Question title', max_length=30)
    body = forms.CharField(label='Question body', max_length=1000)
    tags = forms.CharField(label='Tags', max_length=200)

    class Meta:
        model = Profile
        fields = ["title", "body", "tags"]

    def clean_title(self):
        data_title = self.cleaned_data['title']
        return data_title

    def clean_body(self):
        data_body = self.cleaned_data['body']
        return data_body

    def clean_tags(self):
        data_tag_list = []
        data_tag = self.cleaned_data['tags']
        data_tag_list = data_tag.split()

        return data_tag_list


class AddAnswer(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(), label='Your answer', max_length=10000)

    class Meta:
        model = User
        fields = ["body"]

    def clean_body(self):
        data_body = self.cleaned_data['body']
        return data_body


'''
class QuestionForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
    model = Question
s'''
