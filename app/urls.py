from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.x),
    path('colecoes/',views.c),
    path('lacos-de-repeticao/',views.l),
    path('condicionais/',views.condicionais),
    path('funcoes/',views.funcoes),
    path('modularizacao/',views.modulo),
    path('classes/',views.classes),
]