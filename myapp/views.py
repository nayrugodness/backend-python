from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Categorias, Establecimientos
from .forms import ContactoForm, EstablecimientosForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import EstablecimientosSerializer, CategoriasSerializer
from django.views.generic import ListView, CreateView, DetailView

# Create your views here.


def index(request):
    establecimientos = Establecimientos.objects.all()

    data = {
        'establecimientos': establecimientos
    }

    return render(request, 'app/index.html', data)


def establecimientos(request):

    establecimientos = Establecimientos.objects.all()

    data = {
        'establecimientos': establecimientos
    }

    return render(request, 'app/productos.html', data)


def contacto(request):

    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Mensaje enviado')
        else:
            data['form'] = formulario

    return render(request, 'app/contacto.html', data)


class EstablecimientoDetailView(DetailView):

    template_name = 'app/detalle.html'
    queryset = Establecimientos.objects.all()
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Establecimientos, slug=slug)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Te haz registrado correctamente')
            return redirect(to='index')
        else:
            data['form'] = formulario

    return render(request, 'registration/registro.html', data)


@permission_required('myapp.add_establecimientos')
def agregar_producto(request):
    data = {
        'form': EstablecimientosForm()
    }

    if request.method == 'POST':
        formulario = EstablecimientosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Establecimiento registrado')
        else:
            data['form'] = formulario

    return render(request, 'app/productos/agregar.html', data)


@permission_required('myapp.view_establecimientos')
def listar_producto(request):
    establecimientos = Establecimientos.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        establecimientos = paginator.page(page)

    except:
        raise Http404

    data = {
        'entity': establecimientos,
        'paginator': paginator
    }
    return render(request, 'app/productos/listar.html', data)


@permission_required('myapp.change_productos_w')
def modificar_producto(request, id):
    producto = get_object_or_404(Establecimientos, id=id)

    data = {
        'form': EstablecimientosForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = EstablecimientosForm(
            data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Editado correctamente')
            return redirect(to='listar_producto')
        else:
            data['form'] = formulario

    return render(request, 'app/productos/modificar.html', data)


@permission_required('myapp.delete_productos_w')
def eliminar_producto(request, id):
    producto = get_object_or_404(Establecimientos, id=id)
    producto.delete()
    messages.success(request, 'Eliminado correctamente')
    return redirect(to='listar_producto')


class ProductosViewset(viewsets.ModelViewSet):
    queryset = Establecimientos.objects.all()
    serializer_class = EstablecimientosSerializer

    def get_queryset(self):
        productos = Establecimientos.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        else:
            return productos


class CategoriasViewset(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
