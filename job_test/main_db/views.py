from django.shortcuts import render
from .models import Customer


def main_db(request):
    customer = Customer.objects.all()
    return render(request, 'main_db/main_db.html', {'customer': customer})

def create(request):
    return render(request, 'main_db/create.html')

