from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns =[
    
    path ('agregar_equipo', login_required(views.EquipoCreate.as_view()), name ="agregar_equipo"),
    path ('agregar_jugador', login_required(views.agregar_jugador), name ="agregar_jugador"),
    path ('editar_jugador/<int:pk>', login_required(views.JugadorUpdate.as_view()), name = "editar_jugador"),
    path ('editar_equipo/<int:pk>',login_required(views.EquipoUpdate.as_view()), name = "editar_jugador"),
    path ('listar_equipos',views.listar_equipos, name = "listar_equipos"),
    path ('listar_jugadores', views.listar_jugador,name ="listar_jugadores"),
    path ('borrar_equipo/<int:pk>', login_required(views.EquipoDel.as_view()), name= "borrar_equipo"),
    path ('borrar_jugador/<int:pk>', login_required(views.JugadorDel.as_view()), name = "Borrar_jugador"),
    path ('',views.Pagina_principal,name="pagina_principal" ),
    path ('nominados', views.nominados, name = "nominados"),
    path ('carrito', views.carrito, name = "carrito"),
    path ('modric2018', views.modric2018, name = "modric2018"),
    path ('messi2019', views.messi2019, name = "messi2019"),
    path ('messi2021', views.messi2021, name = "messi2021"),
    path ('messi2023', views.messi2023, name = "messi2023"),
    path ('benzema2022', views.benzema2022, name = "benzema2022"),
    
]
