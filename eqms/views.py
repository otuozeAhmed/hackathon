from django.shortcuts import render
import openpyxl

def index(request):
    return render(request, "index.html")

def equipment_type(request):
    return render(request, "equipment-type.html")

def welcome(request):
    return render(request, "welcome.html")

def tag_details(request):
    return render(request, "tag_details.html")

def oem_details(request):
    return render(request, "oem_details.html")

def equipment_data(request):
    return render(request, "equipment_data.html")

def summary(request):
    data = [1, 2, 3, 4, 5]
    context = {
        "val": data
    }
    return render(request, "summary.html", context)

def units(request):
    return render(request, "units.html")

    