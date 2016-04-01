from django.contrib.auth.models import User
from main.models import Persona
from estudiante.models import Estudiante


def crear_estudiante(strategy, details, response, user, *args, **kwargs):
    username = details['username']
    email =  details['email']
    genero = response['gender']
    url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
    first_name = details['first_name']
    last_name = details['last_name']
    user_object = user
    user_object.first_name = first_name
    user_object.last_name = last_name
    user_object.save()
    if Persona.objects.filter(usuario=user_object).exists():
        if Estudiante.objects.filter(persona__usuario=user_object).exists():
            pass
    else:
        persona = Persona(usuario=user_object)

        persona.tipo_persona = 'E'
        if genero is not None:
            persona.genero = 'F' if genero is 'female' else 'M'
        persona.save()
        estudiante = Estudiante()
        estudiante.persona = persona
        estudiante.foto_facebook_url = url
        estudiante.estado = 'I'
        estudiante.save()
    return kwargs

def associate_by_email(**kwargs):
    try:
        email = kwargs['details']['email']
        kwargs['user'] = User.objects.get(email=email)
    except:
        pass
    return kwargs
