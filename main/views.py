from django.shortcuts import render, redirect, get_object_or_404
from main.models import Categorias, Establecimientos
from main.forms import ContactoForm, EstablecimientosForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from rest_framework import viewsets
from main.serializers import EstablecimientosSerializer, CategoriasSerializer
from django.views.generic import DetailView

# Create your views here.


from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request=request, template_name="hoisu/templates/base.html")