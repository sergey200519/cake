from django.shortcuts import render
from mainapp.models import Cakes
from django.views.generic import DetailView

# Create your views here.
def index(request):
    context = {
        "title": "Главная",
        "cakes": Cakes.objects.all()
    }
    return render(request, "index.html", context=context)

class CakeDetail(DetailView):
    model = Cakes
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Торт"
        return context