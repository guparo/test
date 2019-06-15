from django.shortcuts import render
from .models import Contact
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class ContactList(ListView):
    model = Contact
    template_name = "contact/contact_list.html"
class ContactCreate(CreateView):
    model = Contact
    template_name="contact/contact_form.html"
    fields = ['first_name','last_name', 'email','message']
    success_url = reverse_lazy('home')
