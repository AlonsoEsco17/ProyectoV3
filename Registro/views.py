from django.shortcuts import render, redirect
from .forms import EquipoForm, JugadorForm
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
# Create your views here.

def Pagina_principal(request):
    return render(request,"index.html")

def agregar_equipo(request):
    if request.method=="POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_equipo")
    else:
        form = EquipoForm
        return render(request, "Registro/agregar_equipo.html", {'form': form})

def nominados(request):
    return render(request,"nominados.html")

def carrito(request):
    return render(request,"carrito.html")

def modric2018(request):
    return render(request,"../templates/jugadores/modric2018.html")

def messi2019(request):
    return render(request,"../templates/jugadores/messi2019.html")

def messi2021(request):
    return render(request,"../templates/jugadores/messi2021.html")

def messi2023(request):
    return render(request,"../templates/jugadores/messi2023.html")

def benzema2022(request):
    return render(request,"../templates/jugadores/benzema2022.html")

def agregar_jugador(request):
    if request.method =="POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/listar_jugadores")
    else:
        form = JugadorForm
        return render(request, "Registro/agregar_jugador.html", {'form': form})

def editar_equipo(request, equipo_id):
    instancia= Equipo.objects.get(id=equipo_id)
    form = EquipoForm(instance=instancia)
    if request.method == "POST":
        form = EquipoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request,"Registro/editar_equipo.html", {'form': form})
    

def editar_jugador(request, jugador_id):
    instancia = Jugador.objects.get(id=jugador_id)
    form = JugadorForm(instance=instancia)
    if request.method =="POST":
        form = JugadorForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request,"Registro/editar_jugador.html", {'form' : form})




def listar_jugador(request):
    jugadores = Jugador.objects.all()
    return render(request, "Registro/listar_jugadores.html", {'jugadores': jugadores})

def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request,"Registro/listar_equipos.html", {'equipos': equipos})

def borrar_jugador(request, jugador_id):
    instancia = Jugador.objects.get(id=jugador_id)
    instancia.delete()
    return redirect('listar_jugadores')
    
def borrar_equipo(request, equipo_id):
    isntancia = Equipo.objects.get(id=equipo_id)
    isntancia.delete()
    return redirect('listar_equipos')

   
class EquipoCreate(CreateView):
    model= Equipo
    form_class = EquipoForm
    template_name = 'Registro/agregar_equipo.html'
    success_url = reverse_lazy("listar_equipos")

class EquipoList(ListView):
    model = Equipo
    template_name = 'Registro/listar_equipos.html'

class EquipoUpdate(UpdateView):
    model =  Equipo
    form_class = EquipoForm
    template_name = 'Registro/editar_equipo.html'
    success_url = reverse_lazy('listar_equipos')

class EquipoDel(DeleteView):
    model = Equipo
    template_name = 'Registro/borrar_equipo.html'
    success_url = reverse_lazy('listar_equipos')

class JugadorCreate(CreateView):
    model = Equipo
    form_class = JugadorForm
    template_name = 'Registro/agregar_jugador.html'
    success_url = reverse_lazy('listar_jugadores')
    
class JugadorList(ListView):
    model = Jugador
    template_name = 'Registro/listar_jugadores.html'

class JugadorUpdate(UpdateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'Registro/editar_jugador.html'
    success_url = reverse_lazy('listar_jugadores')

class JugadorDel(DeleteView):
    model = Jugador
    template_name = 'Registro/borrar_jugador.html'
    success_url = reverse_lazy('listar_jugadores')
    
