# users/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Signup View
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'  # Ensure this template exists
    success_url = reverse_lazy('login')  # Redirect to login page after signup


# Login View
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Ensure this template exists


# Home View (Logged-in users only)
@login_required
def home_view(request):
    return render(request, 'home.html', {'username': request.user.username})
