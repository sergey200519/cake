from django import forms

from authapp.models import User

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "gender", "phone", "email", "date_of_birth")
