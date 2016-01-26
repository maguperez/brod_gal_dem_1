from django.contrib.auth.models import User
from main.models import Persona
from estudiante.models import Estudiante


def crear_estudiante(strategy, details, response, user, *args, **kwargs):
    username = details['username']
    email =  details['email']
    user_object = user

    if Persona.objects.filter(usuario=user_object).exists():
        if Estudiante.objects.filter(persona__usuario=user_object).exists():
            pass
    else:
        persona = Persona(usuario=user_object)
        persona.tipo_persona = 'E'
        persona.save()
    return kwargs

def associate_by_email(**kwargs):
    try:
        email = kwargs['details']['email']
        kwargs['user'] = User.objects.get(email=email)
    except:
        pass
    return kwargs
