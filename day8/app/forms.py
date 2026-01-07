from django import forms
from .models import GeeksModel
#defines form class with a single text input field
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget = forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required = False)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text="enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())

class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = "__all__"
        