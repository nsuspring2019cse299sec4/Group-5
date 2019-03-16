from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
	return render(request, 'finddoctor/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/finddoctor')

    else:
        form = UserCreationForm()

    return render(request, 'finddoctor/register.html', {'form': form})
