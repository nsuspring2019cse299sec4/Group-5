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
]