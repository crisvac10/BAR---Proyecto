from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from .serializers import MenuSerializer
from .models import Menu

class ListAPIMenu(ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):

        return Menu.objects.all()