from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-Mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password1'] != cd['password2']:
                raise forms.ValidationError("Пароли не совпадают!")
            return cd['password']

        def clean_email(self):
            email = self.cleaned_data['email']
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError("Такой E-mail уже существует!")
            return email


class LectorRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Логин", max_length=50)
    password = forms.CharField(label="Пароль", max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор пароля", max_length=30, widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password", "password2"]
        labels = {
            'email': 'E-Mail'
        }