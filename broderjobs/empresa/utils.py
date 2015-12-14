from main.models import Persona, GradoEstudio, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma
from empresa.models import Puesto, Empresa, Sector, RankingEmpresa, EvaluacionEmpresa
from oportunidad.models import Oportunidad, Postulacion
from mensaje.models import Mensaje, Mensaje_Destinatario
from django.db.models import Avg


def actualizar_ranking_empresa(empresa_id):
    empresa =  EvaluacionEmpresa.objects.filter(empresa_id = empresa_id).aggregate(Avg('ranking'),
                                                                    Avg('linea_carrera'),
                                                                    Avg('flexibilidad_horarios'),
                                                                    Avg('ambiente_trabajo'),
                                                                    Avg('salarios'))
    e, created = RankingEmpresa.objects.get_or_create(empresa_id = empresa_id)
    e.linea_carrera = empresa["linea_carrera__avg"]
    e.flexibilidad_horarios = empresa["flexibilidad_horarios__avg"]
    e.ambiente_trabajo = empresa["ambiente_trabajo__avg"]
    print(empresa["salarios__avg"])
    e.salarios = empresa["salarios__avg"]
    e.ranking_general = empresa["ranking__avg"]
    e.save()

