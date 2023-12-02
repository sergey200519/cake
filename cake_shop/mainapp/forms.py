from django import forms
from mainapp.models import Reviews

class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ("rating", "text")
    
    def __init__(self,*args,**kwargs):
        super(ReviewsForm, self).__init__(*args,**kwargs)

        for filed_name , field in self.fields.items():
            field.required=True
        
        self.fields["rating"].widget.attrs["class"] = "none reviews__rating_input"
        self.fields["text"].widget.attrs["class"] = "reviews__textarea"
        self.fields["text"].widget.attrs["placeholder"] = "Сообщение"
        
