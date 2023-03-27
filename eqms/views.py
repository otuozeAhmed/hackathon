from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def equipment_type(request):
    return render(request, "equipment-type.html")

def welcome(request):
    return render(request, "ui-buttons.html")

def tag_details(request):
    return render(request, "bootstrap-tables.html")

def oem_details(request):
    return render(request, "oem_details.html")