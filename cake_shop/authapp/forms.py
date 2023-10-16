from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from authapp.models import User

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ("phone", "password")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
        self.fields["username"].widget.attrs["class"] = "login__form__input"
        self.fields["password"].widget.attrs["class"] = "login__form__input"

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1','password2','last_name','first_name','email', "phone")

    def __init__(self,*args,**kwargs):
        super(UserRegisterForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ведите фамилию'
        self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Введите ваш телефон'