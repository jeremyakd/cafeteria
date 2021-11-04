from django.shortcuts import render
from .models import Service

def services(request):
    servicios = Service.objects.all()
    return render(request, 'services/services.html', { 'servicios': servicios })