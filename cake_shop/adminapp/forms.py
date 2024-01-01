from django import forms
from django.forms import BaseFormSet

from mainapp.models import Products, ProductCategories, ImgProducts, SwiperSlides

from adminapp.models import Applications


class CreateProductForm(forms.Form):
    def __init__(self,*args,**kwargs):
        super(CreateProductForm, self).__init__(*args,**kwargs)
    
    name = forms.CharField(label="Наименование продукта", required=True)
    ingredients = forms.CharField(max_length=128, required=True)
    # price = forms.FloatField(min_value=0, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    category = forms.ModelChoiceField(queryset=ProductCategories.objects.all(), required=True)

    article_four_hundred = forms.IntegerField(max_value=10000, required=True)
    price_four_hundred = forms.FloatField(min_value=0, required=True)

    article_six_hundred = forms.IntegerField(max_value=10000, required=True)
    price_six_hundred = forms.FloatField(min_value=0, required=True)

    article_eight_hundred = forms.IntegerField(max_value=10000, required=True)
    price_eight_hundred = forms.FloatField(min_value=0, required=True)

    article_one_thousand = forms.IntegerField(max_value=10000, required=True)
    price_one_thousand = forms.FloatField(min_value=0, required=True)

    article_two_thousand = forms.IntegerField(max_value=10000, required=True)
    price_two_thousand = forms.FloatField(min_value=0, required=True)

    def __init__(self,*args,**kwargs):
        super(CreateProductForm, self).__init__(*args,**kwargs)


        for filed_name , field in self.fields.items():
            field.widget.attrs["class"] = "addproduct__form__input"
            field.required=True
        self.fields["description"].widget.attrs["class"] = "addproduct__form__input addproduct__form__textarea"


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
        self.fields["files"].widget.attrs["multiple"] = "multiple"
        self.fields["files"].widget.attrs["class"] = "inputfile"
        self.fields["files"].widget.attrs["id"] = "file"
        self.fields["files"].widget.attrs["name"] = "file"
        self.fields["files"].widget.attrs["data-multiple-caption"] = "{count} файлов выбрано"



class CategoryCreateForm(forms.ModelForm):
    
    class Meta:
        model = ProductCategories
        fields = ("name",)

    def __init__(self,*args,**kwargs):
        super(CategoryCreateForm, self).__init__(*args,**kwargs)
        self.fields["name"].widget.attrs["class"] = "addcategories__form__input"

class SlidesForm(forms.ModelForm):
    
    class Meta:
        model = SwiperSlides
        fields = ("title", "description", "img")

    def __init__(self,*args,**kwargs):
        super(SlidesForm, self).__init__(*args,**kwargs)

        self.fields["img"].widget.attrs["class"] = "inputfile"
        self.fields["img"].widget.attrs["name"] = "file"
        self.fields["img"].widget.attrs["id"] = "file"
        self.fields["img"].widget.attrs["data-multiple-caption"] = "{count} файлов выбрано"

        self.fields["title"].widget.attrs["class"] = "addslider__form__input"
        self.fields["description"].widget.attrs["class"] = "addslider__form__input"




class ApplicationsForm(forms.ModelForm):

    class Meta:
        model = Applications
        fields = ("username", "email", "report")

    def __init__(self,*args,**kwargs):
        super(ApplicationsForm, self).__init__(*args,**kwargs)

        self.fields["username"].widget.attrs["placeholder"] = "Фамилия, имя и отчество"
        self.fields["email"].widget.attrs["placeholder"] = "E-mail*"
        self.fields["report"].widget.attrs["placeholder"] = "Сообщение"