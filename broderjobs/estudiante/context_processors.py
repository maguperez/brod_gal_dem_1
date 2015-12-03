from .models import Estudiante
from main.models import Persona


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
