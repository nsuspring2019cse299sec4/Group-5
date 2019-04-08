from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views import generic
from .models import Disease, Doctor
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

class DiseaseView(generic.ListView):
	template_name = 'finddoctor/disease.html'

	def get_queryset(self):
		return Disease.objects.all()

class TreatmentView(generic.DetailView):
	model = Disease
	template_name = 'finddoctor/treatment.html'

	#def get_queryset(self):
		#return Disease.objects.all()

class DoctorView(generic.DetailView):
	model = Doctor
	template_name = 'finddoctor/doctor.html'



