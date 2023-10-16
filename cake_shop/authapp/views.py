from django.shortcuts import render

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse


from authapp.forms import UserLoginForm, UserRegisterForm
from authapp.models import User

from django.db.models import Q

# Create your views here.
def login(request):
    
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            pass
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    username = request.POST.get("username")
    password = request.POST.get("password")
    print(f"form is valid {username} and password is {password}")
    user = auth.authenticate(request, phone=username)
    user = User.objects.get(
                 Q(email=username) | Q(phone=username)
             )
    print(user)
    if user is not None:
        pwd_valid = user.check_password(password)
        print(user, pwd_valid)
        if pwd_valid and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("mainapp:index"))


    # context = {
    #     "title": "Вход",
    #     "form": form
    # }
    # return  render(request, "authapp/login.html", context=context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("authapp:login"))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {
        "title": "Регистрация",
        "form": form
    }
    return render(request, "authapp/register.html", context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("mainapp:index"))