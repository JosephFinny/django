# users/urls.py
from django.urls import path
from .views import SignupView, CustomLoginView, home_view

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', home_view, name='home'),
]
