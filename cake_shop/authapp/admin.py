from django.contrib import admin

from authapp.models import User, ImgUser

# Register your models here.
admin.site.register(User)
admin.site.register(ImgUser)