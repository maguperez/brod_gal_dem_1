from .models import Estudiante
from main.models import Persona
from mensaje.models import Mensaje_Destinatario, Notificacion


def estudiante_foto(request):
    estudiante_foto = 'url'
    if request.user.is_authenticated():
        persona = Persona.objects.get(usuario_id = request.user)
        if persona.tipo_persona == 'E':
            try:
                estudiante = Estudiante.objects.get(persona_id = persona.id)
            except Estudiante.DoesNotExist:
                estudiante = None
            if estudiante is not None:
                estudiante = Estudiante.objects.get(persona_id = persona.id)
                estudiante_foto = estudiante.set_foto
    return {'estudiante_foto': estudiante_foto}

def mensajes_actuales(request):
    cantidad_mensajes = Mensaje_Destinatario.objects.filter(leido = False, usuario_destinatario = request.user.id).count()
    mensajes = Mensaje_Destinatario.objects.filter(leido = False, usuario_destinatario = request.user.id)
    return {'cantidad_mensajes': cantidad_mensajes, 'mensajes': mensajes}

def notificaciones(request):
    cantidad_notificaciones = Notificacion.objects.filter(leido = False, usuario_destinatario = request.user.id).count()
    notificaciones = Notificacion.objects.filter(usuario_destinatario = request.user.id).order_by("-fecha_envio")[:10]
    return {'cantidad_notificaciones': cantidad_notificaciones, 'notificaciones': notificaciones}
