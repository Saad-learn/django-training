from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label="Student Name", 
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    age = forms.IntegerField(
        min_value=1,
        max_value=100
        )
    feedback = forms.CharField(
        widget = forms.Textarea(attrs={"rows":4})
    )
    agree = forms.BooleanField(label="I agree to terms")