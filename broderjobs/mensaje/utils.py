# coding=utf-8
from .models import Mensaje, Mensaje_Destinatario, Notificacion
from oportunidad.models import Oportunidad, Postulacion, ProcesoFase
from estudiante.models import Estudiante
from main.models import Persona
from datetime import date, datetime

def enviar_mensaje_multiple_estudiantes(oportunidad, ususrio_remitente, ids_estudiantes, asunto, contenido, permite_respuesta, es_respuesta):
    mensaje = Mensaje()
    mensaje.oportunidad = oportunidad
    mensaje.usuario_remitente = ususrio_remitente
    mensaje.asunto = asunto
    mensaje.contenido = contenido
    mensaje.permite_respuesta = permite_respuesta
    mensaje.es_respuesta = es_respuesta
    mensaje.fecha_envio = datetime.now()

    mensaje.fecha_creacion = datetime.now()
    mensaje.usuario_creacion = ususrio_remitente.username
    mensaje.save()

    #Mensaje Destinatarios
    for id in ids_estudiantes:
        estudiante = Estudiante.objects.get(id = id)
        mensaje_destinatarios = Mensaje_Destinatario()
        mensaje_destinatarios.mensaje = mensaje
        mensaje_destinatarios.usuario_destinatario = estudiante.persona.usuario
        mensaje_destinatarios.fecha_envio = datetime.now()
        mensaje_destinatarios.fecha_creacion = datetime.now()
        mensaje_destinatarios.save()
        enviar_notificacion(oportunidad, estudiante.persona.usuario, asunto, True, ususrio_remitente.username)

def enviar_mensaje(oportunidad, ususrio_remitente, usuario_destinatario, asunto, contenido, permite_respuesta, es_respuesta):
    mensaje = Mensaje()
    mensaje.oportunidad = oportunidad
    mensaje.usuario_remitente = ususrio_remitente
    mensaje.asunto = asunto
    mensaje.contenido = contenido
    mensaje.permite_respuesta = permite_respuesta
    mensaje.es_respuesta = es_respuesta
    mensaje.fecha_envio = datetime.now()
    if es_respuesta is not None:
        mensaje.es_respuesta = es_respuesta

    mensaje.fecha_creacion = datetime.now()
    mensaje.usuario_creacion = ususrio_remitente.username
    mensaje.save()

    #Mensaje Destinatarios
    mensaje_destinatarios = Mensaje_Destinatario()
    mensaje_destinatarios.mensaje = mensaje
    mensaje_destinatarios.usuario_destinatario = usuario_destinatario
    mensaje_destinatarios.fecha_envio = datetime.now()
    mensaje_destinatarios.save()
    enviar_notificacion(oportunidad, usuario_destinatario, asunto, True, ususrio_remitente.username)

def enviar_notificacion(oportunidad, usuario_destinatario, asunto, es_mensaje, usuario_creacion):

    persona = Persona.objects.get(usuario_id = usuario_destinatario.id)
    notificacion = Notificacion()

    if persona.tipo_persona == 'E':
        postulacion = Postulacion.objects.get(oportunidad_id = oportunidad.id, estudiante__persona = persona.id)
        notificacion.postulacion = postulacion

    notificacion.oportunidad = oportunidad
    notificacion.usuario_destinatario = usuario_destinatario
    notificacion.asunto = asunto
    notificacion.es_mensaje = es_mensaje
    notificacion.fecha_envio = datetime.now()
    notificacion.fecha_creacion = datetime.now()
    notificacion.usuario_creacion = usuario_creacion
    notificacion.save()

def enviar_notificacion_multiple_estudiantes(oportunidad, ids_estudiantes, asunto, es_mensaje, usuario_creacion):
    for id in ids_estudiantes:
        estudiante = Estudiante.objects.get(id = id)
        postulacion = Postulacion.objects.get(oportunidad_id = oportunidad.id, estudiante_id = estudiante.id)
        notificacion = Notificacion()
        notificacion.oportunidad = oportunidad
        notificacion.postulacion = postulacion
        notificacion.usuario_destinatario = estudiante.persona.usuario
        notificacion.asunto = asunto
        notificacion.es_mensaje = es_mensaje
        notificacion.usuario_creacion = usuario_creacion
        notificacion.fecha_creacion = datetime.now()
        notificacion.fecha_creacion = datetime.now()
        notificacion.save()
