from django.shortcuts import render
from .models import DisplayCarsModel

# Create your views here.

#our home view
def index(request):
    return render(request, "index.html")

#our services view
def services(request):
    return render(request, "services.html")

#our cars view
def cars(request):
    
    display_cars = DisplayCarsModel.objects.all #fetching the car data from the database using the display car model

    return render(request, "cars.html", {'display_cars': display_cars}) #passing our objects as well

#our faq view
def faq(request):
    return render(request, "faq.html")

#our about us view
def about(request):
    return render(request, "about.html")

#our contact view
def contact(request):
    return render(request, "contact.html")
