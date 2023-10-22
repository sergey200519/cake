from django.views.generic import ListView, UpdateView
from django.shortcuts import render, redirect

from authapp.models import User
from profileapp.forms import ProfileForm

from django.urls import reverse, reverse_lazy

# Create your views here.
class ProfileListView(ListView):
    model = User
    template_name = "profileapp/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Профиль"
        print(User.objects.all())
        return context

def profile_edit(request, pk):
    user_up = User.objects.get(id=pk)
    data = {
        "first_name": user_up.first_name,
        "last_name": user_up.last_name,
        "date_of_birth": user_up.date_of_birth,
        "gender": user_up.gender,
        "phone": user_up.phone,
        "email": user_up.email
    }
    if request.method == "POST":
        
        form = ProfileForm(request.POST)
        if form.is_valid():
            data = form.data
            user_up.first_name = data["first_name"]
            user_up.last_name = data["last_name"]
            user_up.date_of_birth = data["date_of_birth"]
            user_up.gender = data["gender"]
            user_up.phone = data["phone"]
            user_up.email = data["email"]
            user_up.save()
            # data = form.data
            # product.name = data["name"]
            
        else:
            print(form.errors)

    
    context = {
        "title": "Админка | Изменение",
        "form": ProfileForm(data)
    }

    return render(request,"profileapp/profile_edit.html",context)


class ProfileFormView(UpdateView):
    # model = User
    template_name = 'authapp/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profileapp:profile_list')
    title = 'Gekshop | Профайл'

    def post(self, request, *args, **kwargs):
        form = ProfileForm(data=request.POST, files=request.FILES,
                               instance=request.user)
        profile_form = ProfileForm(data=request.POST,
                                           files=request.FILES,
                                           instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data()
        context['profile'] = UserProfileEditForm(
            instance=self.request.user.userprofile)
        return context
