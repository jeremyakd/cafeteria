from django.db import reset_queries
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            print("Nombre: {} , Email: {} , Contenido: {}.".format(name, email, message))
            return redirect(reverse('contact')+'?ok' )

    return render(request, 'contact/contact.html',
        { 'formulario': contact_form }
    )
