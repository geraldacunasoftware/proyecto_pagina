from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request,'index.html')

def enviar_correo(request):
    if request.method == 'POST':
        nombre = request.POST.get('txt-name')
        correo = request.POST.get('txt-email')
        subject = request.POST.get('txt-subject')
        mensaje = request.POST.get('txt-message')

        # Mensaje para enviar por correo
        asunto = f"Asunto de correo: {subject}"
        contenido = f"Mensaje de: {nombre} ({correo})\n\n{mensaje}"

        try:
            send_mail(asunto, contenido, settings.EMAIL_HOST_USER, ['geraldacunasoftware@gmail.com'])
            return redirect('index')  # Redirecciona a una página de éxito
        except Exception as e:
            print("Error al enviar el correo:", e)  # Esto ayuda a ver el error en la consola
            return render(request,'contact.html', {'error': 'No se pudo enviar el correo. Inténtalo de nuevo más tarde.'})

    return render(request,'contact.html')

# Create your views here.

    
def contact(request):
    return render(request,'contact.html')

