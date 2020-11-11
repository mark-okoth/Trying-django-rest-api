from django.shortcuts import render
from rest_framework import viewsets
from .models import Countries
from .serializer import CountriesSerializer

# Create your views here.
class CountriesView(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer