from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.base import View


class CustomDispatchMixin(View):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CustomDispatchMixin,self).dispatch(request, *args, **kwargs)
    
class UserDispatchMixin(View):
    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDispatchMixin,self).dispatch(request, *args, **kwargs)