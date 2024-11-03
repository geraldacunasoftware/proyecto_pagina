from django.urls import path
from .views import contact,enviar_correo

urlpatterns = [
    path('contact',contact,name='contact'),
    path('enviar_correo',enviar_correo,name='enviar_correo'),
]
