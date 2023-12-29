from django import forms
from django.db import models

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from authapp.models import User, ImgUser
from phonenumber_field.modelfields import PhoneNumberField

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ("phone", "password")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
        self.fields["username"].widget.attrs["class"] = "login__form__input formInput"
        self.fields["username"].widget.attrs["id"] = "login__tel"
        self.fields["password"].widget.attrs["class"] = "login__form__input formInput"
        self.fields["password"].widget.attrs["id"] = "password"

class DateInput(forms.DateInput):
    input_type = "date"

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","password1","password2","last_name","first_name",
                  "patronymic","email", "phone","gender","address","date_of_birth")

    def __init__(self,*args,**kwargs):
        super(UserRegisterForm, self).__init__(*args,**kwargs)

        self.fields["gender"] = forms.CharField(max_length=50)
        self.fields["date_of_birth"] = forms.DateField(widget=DateInput,required=True)


        for filed_name , field in self.fields.items():
            field.widget.attrs["class"] = "register__form__input"
            field.required=True
        
        self.fields["gender"].widget.attrs["class"] = "gender_value none"
        self.fields["username"].widget.attrs["id"] = "username_input"
        self.fields["date_of_birth"].widget.attrs["class"] = "register__form__input register__form__input_date"
        self.fields["password2"].widget.attrs["class"] = "register__form__input width-200 register__form__input_date"
        
class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("image", "first_name", "last_name", "patronymic",
                  "username", "date_of_birth", "gender", "phone",
                  "email", "address")
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields["date_of_birth"] = forms.DateField(widget=DateInput,required=True)
        
        # self.fields["image"] = forms.ImageField()
        
        for filed_name , field in self.fields.items():
            field.widget.attrs["class"] = "form__input"
            field.widget.attrs["id"] = f"id_{filed_name}_profile"
        
        self.fields["gender"].widget.attrs["class"] = "none profile_gender"

        self.fields["date_of_birth"].widget.attrs["class"] = "form__input date_of_birth_profile"

        self.fields["image"].widget.attrs["class"] = "none"
        self.fields["image"].widget.attrs["id"] = "mypage__photoi"
        self.fields["image"].widget.attrs["accept"] = ".jpg,.jpeg,.svg,.png"



