from .models import Pregunta, Respuesta, EstudianteRespuestas, DiscCodificacion, EstudiantePatron, PatronPerfil


def obtener_patron(estudiante):
    D_mas = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id, letra_mas = 'D').count()
    D_menos = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id, letra_menos = 'D').count()
    I_mas = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id, letra_mas = 'I').count()
    I_menos = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id, letra_menos = 'I').count()
    S_mas = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id, letra_mas = 'S').count()
    S_menos = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id, letra_menos = 'S').count()
    C_mas = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id, letra_mas = 'C').count()
    C_menos = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id, letra_menos = 'C').count()

    total_D = D_mas - D_menos
    total_I = I_mas - I_menos
    total_S = S_mas - S_menos
    total_C = C_mas - C_menos

    # esto se elimina una vez que se tenga los patrones cargados
    estudiante_patron, created = EstudiantePatron.objects.get_or_create(estudiante_id = estudiante.id)
    if created is True:
        estudiante_patron.estudiante = estudiante
    estudiante_patron.total_d = total_D
    estudiante_patron.total_i = total_I
    estudiante_patron.total_s = total_S
    estudiante_patron.total_c = total_C
    estudiante_patron.save()
    try:
        D = DiscCodificacion.objects.get(letra ='D', valor_desde__lte = total_D, valor_hasta__gte= total_D)
        I = DiscCodificacion.objects.get(letra ='I', valor_desde__lte = total_I, valor_hasta__gte= total_I)
        S = DiscCodificacion.objects.get(letra ='S', valor_desde__lte = total_S, valor_hasta__gte= total_S)
        C = DiscCodificacion.objects.get(letra ='C', valor_desde__lte = total_C, valor_hasta__gte= total_C)
        nro_patron = str(D.segmento)+str(I.segmento)+str(S.segmento)+str(C.segmento)
        patron_perfil = PatronPerfil.objects.get(nro_patron = nro_patron)
        estudiante_patron.patron = nro_patron
        estudiante_patron.patron_perfil = patron_perfil
        estudiante_patron.save()
        if patron_perfil.no_concluyente == True:
            resp = "-1"
    except:
        nro_patron = "-1"
        # resp = EstudianteRespuestas.objects.filter(estudiante_id = estudiante.id).delete()
    return nro_patron