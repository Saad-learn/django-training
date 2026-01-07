from django.shortcuts import render
from .forms import StudentForm

def student_form_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, "success.html", {"data": data})
    else:
        form = StudentForm()

    return render(request, "student_form.html", {"form": form})
