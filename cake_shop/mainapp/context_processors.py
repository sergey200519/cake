from adminapp.forms import ApplicationsForm

from django.core.mail import EmailMultiAlternatives



def report_form(request):
    if request.method == "POST":
        report_form = ApplicationsForm(request.POST)
        print("ggfg", report_form.is_valid())
        if report_form.is_valid():
            print("form is valid")
            report_form.save()
            print("email")
            msg = EmailMultiAlternatives(subject="test", to=["oborok05@bk.ru",])
            msg.attach_alternative("html_content", "text/html")
            msg.send()



    report_form = ApplicationsForm()
    return {"report_form": report_form}