from authapp.forms import UserLoginForm, UserRegisterForm



def base_context(request):
    login_form = UserLoginForm()
    register_form = UserRegisterForm()
    context = {
        "login_form": login_form,
        "register_form": register_form
    }
    return context