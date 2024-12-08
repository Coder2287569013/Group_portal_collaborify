from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import Group
from .models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.
class RegisterView(CreateView): # - RegisterView for registering new users
    model = CustomUser
    template_name = 'auth_sys/register_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        group, created = Group.objects.get_or_create(name="Student")
        user = form.save(commit=False)
        user.role = group
        user.save()
        login(self.request, user)

        return redirect('main')

class CustomLoginView(LoginView):
    template_name = 'auth_sys/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = 'main'