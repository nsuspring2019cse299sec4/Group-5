from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

#needs to register
app_name = 'finddoctor'

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', LoginView.as_view(template_name='finddoctor/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('finddoctor:login')), name="logout"),
    path('register/', views.register, name='register'),
    path('disease/', views.DiseaseView.as_view(), name='disease'),
    path('<int:pk>/',views.TreatmentView.as_view(), name='treatment'),
    path('doctor/<int:pk>/',views.DoctorView.as_view(), name='doctor'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='index'),
    path('appoinmentlist/', views.AppoinmentlistView.as_view(), name='appoinmentlist'),
]