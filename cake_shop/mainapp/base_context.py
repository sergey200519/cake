from authapp.models import ImgUser
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm



def base_context(request):
    login_form = UserLoginForm()
    register_form = UserRegisterForm()
    
    user = request.user
    if user.is_authenticated:
        data = {
            # "image": user.image.url,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "patronymic": user.patronymic,
            "username": user.username,
            "date_of_birth": user.date_of_birth,
            "gender": user.gender,
            "phone": user.phone,
            "email": user.email,
            "address": user.address
        }


        profile_form = UserProfileForm(data)
        context = {
            "login_form": login_form,
            "register_form": register_form,
            "profile_form": profile_form,
        }
    else:
        context = {
            "login_form": login_form,
            "register_form": register_form,
        }
    return context