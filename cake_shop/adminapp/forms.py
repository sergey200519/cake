from django import forms
from django.forms import BaseFormSet

from mainapp.models import Products, ProductCategories, ImgProducts
from adminapp.models import Applications


def get_categories_for_ChoiceField():
        categories = []
        for category in ProductCategories.objects.all():
            temp = (category.id, category.name)
            categories.append(temp)
        print(f"{categories}--------------------------------------------->forms")
        return categories



class CreateProductForm(forms.Form):
    def __init__(self,*args,**kwargs):
        # print(categories)
        super(CreateProductForm, self).__init__(*args,**kwargs)
    
    name = forms.CharField(label="Наименование продукта", widget=forms.Textarea, required=True)
    ingredients = forms.CharField(max_length=128, required=True)
    quantity = forms.IntegerField(min_value=0, required=True)
    price = forms.FloatField(min_value=0, required=True)
    # category = forms.ChoiceField(choices=get_categories_for_ChoiceField(), required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    category = forms.ModelChoiceField(queryset=ProductCategories.objects.all(), required=True)
    
    # class Meta:
    #     model = Products
    #     fields = ('name','ingredients','price','category')

# class ImageForm(forms.Form):
#     image = forms.ImageField(label='Image')    
    # class Meta:
    #     model = ImgProducts
    #     fields = ('image', )
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = ImgProducts
        fields = ('image', )


class BaseArticleFormSet(BaseFormSet):
        def add_fields(self, form, index):
            super().add_fields(form, index)
            form.fields["image"] = forms.ImageField(label='Image')



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class UploadFileForm(forms.Form):
    files = MultipleFileField(required=False)

    def __init__(self,*args,**kwargs):
        super(UploadFileForm, self).__init__(*args,**kwargs)
        self.fields['files'].widget.attrs['multiple'] = 'multiple'



class ApplicationsForm(forms.ModelForm):

    class Meta:
        model = Applications
        fields = ("email", "report")

    # def __init__(self,*args,**kwargs):
    #     super(UserAdminRegisterForm, self).__init__(*args,**kwargs)
    #     self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
    #     self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
