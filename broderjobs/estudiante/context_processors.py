from .models import Estudiante
from main.models import Persona
from mensaje.models import Mensaje_Destinatario, Notificacion
from disc.models import EstudiantePatron


def estudiante_foto(request):
    completo_test = False
    no_concluyente_test = False
    estudiante_foto = 'url'
    completo_test= 0
    if request.user.is_authenticated():
        try:
            persona = Persona.objects.get(usuario_id = request.user)
            if persona.tipo_persona == 'E':
                try:
                    estudiante = Estudiante.objects.get(persona_id = persona.id)
                except Estudiante.DoesNotExist:
                    estudiante = None
                if estudiante is not None:
                    estudiante = Estudiante.objects.get(persona_id = persona.id)
                    estudiante_foto = estudiante.set_foto
                    completo_test = estudiante.completo_test
                    try:
                        estudiante_patron = EstudiantePatron.objects.get(estudiante_id = estudiante.id)
                        no_concluyente_test = estudiante_patron.patron_perfil.perfil.no_concluyente
                    except EstudiantePatron.DoesNotExist:
                        no_concluyente_test = False
        except Persona.DoesNotExist:
            completo_test = False
            estudiante_foto = 'url'

    return {'estudiante_foto': estudiante_foto, 'completo_test': completo_test, 'no_concluyente_test': no_concluyente_test}

def mensajes_actuales(request):
    cantidad_mensajes = Mensaje_Destinatario.objects.filter(leido = False, usuario_destinatario = request.user.id).count()
    mensajes = Mensaje_Destinatario.objects.filter(leido = False, usuario_destinatario = request.user.id)
    return {'cantidad_mensajes': cantidad_mensajes, 'mensajes': mensajes}

def notificaciones(request):
    cantidad_notificaciones = Notificacion.objects.filter(leido = False, usuario_destinatario = request.user.id).count()
    notificaciones = Notificacion.objects.filter(usuario_destinatario = request.user.id).order_by("-fecha_envio")[:10]
    return {'cantidad_notificaciones': cantidad_notificaciones, 'notificaciones': notificaciones}
