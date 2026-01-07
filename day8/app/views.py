from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm, InputForm
from django.core.mail import send_mail

# Create your views here.
def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if  form.is_valid():
            return HttpResponseRedirect("/thanks")
        else:
            form = NameForm()
        return render(request, "name.html", {"form": form })
    
    if form.is_valid():
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        sender = form.cleaned_data["sender"]
        cc_myself = form.cleaned_data["cc_myself"]

        recipients = ["info@example.com"]
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect("/thanks/")

# def index(request):
#     form = MyForm()
#     rendered_form = form.render("form_snipet.html")
#     context = {"form" : rendered_form}
#     return render(request, "index.html", context)

# class home_view(request):
    # context = {}
    # context['form'] = InputForm()
    # return render(request, 'home.html', context)
