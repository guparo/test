from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreate
from django.views import generic

#from .forms import ContactForm

class UserRegister(CreateView):
    model = User
    template_name = "myusers/user_create.html"
    form_class = UserCreate
    success_url = reverse_lazy('chart')


class UsersListView(generic.ListView):
    model = User
    template_name = "myusers/user_list.html"