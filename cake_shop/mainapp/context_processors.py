from adminapp.forms import ApplicationsForm


def report_form(request):
    if request.method == "POST":
        report_form = ApplicationsForm(request.POST)
        if report_form.is_valid():
            report_form.save()



    report_form = ApplicationsForm()
    return {"report_form": report_form}