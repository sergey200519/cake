from django import forms

from orderapp.models import Order


class CreateOrder(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ("status_completed", "status_owner", "date", "discount", "summ", "total_summ", "user")

    def __init__(self,*args,**kwargs):
        super(CreateOrder, self).__init__(*args,**kwargs)


        for filed_name , field in self.fields.items():
            field.widget.attrs["class"] = "form__input"
            field.required = True

        self.fields["phone"].widget.attrs["class"] = "tel form__input"

        self.fields["status_delivery"].widget.attrs["id"] = "order_delivery_status"
        self.fields["status_delivery"].widget.attrs["class"] = "none"

        self.fields["promo_code"].required = False