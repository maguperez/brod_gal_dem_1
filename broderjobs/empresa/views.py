# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Puesto, Empresa, Representante, Sector, Picture, EmpresaRedesSociales, VideoUrl
from main.models import Persona, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma
from oportunidad.models import Oportunidad, Postulacion
from estudiante.models import Estudiante, Resumen, ActividadesExtra, ExperienciaProfesional, Voluntariado, ConocimientoExtra
from django.core.paginator import Paginator, InvalidPage
from django.template import RequestContext
from django.db.models import Q, CharField
from empresa import utils
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
import json
from cStringIO import StringIO
from django.views.generic import CreateView, DeleteView, ListView
from .response import JSONResponse, response_mimetype
from .serialize import serialize
from main.utils import LoginRequiredMixin, calular_edad
from django.core.paginator import InvalidPage, Paginator
from datetime import date,datetime

# import ho.pisa as pisa
# import cStringIO as StringIO
# import cgi
from django.template.loader import render_to_string

# Create your views here.
@login_required(login_url='/empresa-registro/')
def oportunidad_listar(request):
    user = request.user
    persona = Persona.objects.get(usuario_id=user.id)
    representante = get_object_or_404(Representante, persona_id =persona.id)

    return render(request, 'empresa/oportunidades-listar.html')

class MiEmpresaView(FormView):
    form_class = forms.LogoForm
    template_name = 'empresa/mi-empresa.html'
    success_url = reverse_lazy('mi-empresa')

    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        oportunidades =  Oportunidad.objects.filter(empresa_id = empresa.id)[:3]
        # imagenes = Picture.objects.filter(empresa_id = empresa.id)
        # videos = VideoUrl.objects.filter(empresa_id = empresa.id)

        redes_sociales, crear =EmpresaRedesSociales.objects.get_or_create(empresa_id=representante.empresa.id, estado = 'A')
        if crear:
            redes_sociales.empresa = representante.empresa
            redes_sociales.save()

        context = super(MiEmpresaView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidades'] = oportunidades
        # context['imagenes'] = imagenes
        context['redes_sociales'] = redes_sociales
        # context['videos'] = videos

        return context

    def form_valid(self, form):
        try:
            logo = self.request.FILES['logo']
        except:
            logo= None
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id=persona.id)
        empresa = Empresa.objects.get(representante = representante.id)
        if logo is not None:
            empresa.logo = logo
        else:
            empresa.logo.delete()
        empresa.save()
        return super(MiEmpresaView, self).form_valid(form)

class AjaxTemplateMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            #split[-1] = '-inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
            if request.is_ajax():
                self.template_name = self.ajax_template_name
            return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class InfoGeneralView(FormView):

        form_class = forms.InfoGeneralForm
        template_name = 'empresa/mi-empresa-info-general.html'
        success_url = reverse_lazy('mi-empresa')

        def get_initial(self):

            user = self.request.user
            persona = Persona.objects.get(usuario_id=user.id)
            representante =get_object_or_404(Representante, persona_id =persona.id)
            empresa = Empresa.objects.get(id=representante.empresa.id)
            return {
                'nombre': empresa.nombre,
                'quienes_somos': empresa.quienes_somos,
                'RUC': empresa.RUC,
                'telefono':empresa.telefono,
                'sector': empresa.sector,
                'numero_funcionarios': empresa.numero_funcionarios,
                'facturacion_anual': empresa.facturacion_anual,
                'ano_fundacion': empresa.ano_fundacion,
                'website': empresa.website,
                'pais': empresa.pais,
                'ciudad_hidden': '' if empresa.ciudad is None else empresa.ciudad.id}

        def form_invalid(self, form):
            return 'form.errors'

        def form_valid(self, form):
            nombre =  form.cleaned_data['nombre']
            quienes_somos =  form.cleaned_data['quienes_somos']
            RUC = form.cleaned_data['RUC']
            sector = form.cleaned_data['sector']
            pais = form.cleaned_data['pais']
            id_ciudad = form.cleaned_data['ciudad_hidden']
            telefono = form.cleaned_data['telefono']

            numero_funcionarios = form.cleaned_data['numero_funcionarios']
            facturacion_anual = form.cleaned_data['facturacion_anual']

            ano_fundacion = form.cleaned_data['ano_fundacion']
            website = form.cleaned_data['website']

            user = self.request.user
            persona = Persona.objects.get(usuario_id=user.id)
            representante = Representante.objects.get(persona_id =persona.id)
            empresa = Empresa.objects.get(id=representante.empresa.id)

            empresa.nombre = nombre
            empresa.quienes_somos = quienes_somos
            empresa.RUC = RUC
            empresa.sector = sector
            empresa.numero_funcionarios = numero_funcionarios
            empresa.facturacion_anual = facturacion_anual
            empresa.ano_fundacion = ano_fundacion
            empresa.website =website
            empresa.pais = pais
            empresa.telefono = telefono

            if id_ciudad is not None and id_ciudad != '':
                try:
                    ciudad = Ciudad.objects.get(id = id_ciudad)
                except Ciudad.DoesNotExist:
                    ciudad = None
                if ciudad is not None:
                    empresa.ciudad = ciudad
            else:
                empresa.ciudad = None
            # empresa.ciudad = ciudad
            empresa.save()

            return super(InfoGeneralView, self).form_valid(form)

class RedesSocialesView(FormView):

    form_class = forms.RedesSocialesForm
    template_name = 'empresa/mi-empresa-redes-sociales.html'
    success_url = reverse_lazy('mi-empresa')

    def get_initial(self):

        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        try:
            redes_empresa, crear =EmpresaRedesSociales.objects.get_or_create(empresa_id=representante.empresa.id, estado = 'A')
            if crear:
                redes_empresa.empresa = representante.empresa
                redes_empresa.save()
        except EmpresaRedesSociales.DoesNotExist:
            redes_empresa = EmpresaRedesSociales()
        return {
            'facebook': redes_empresa.facebook,
            'twitter': redes_empresa.twitter,
            'linkedin': redes_empresa.linkedin}

    def form_invalid(self, form):
        return 'form.errors'

    def form_valid(self, form):
        facebook =  form.cleaned_data['facebook']
        twitter = form.cleaned_data['twitter']
        linkedin = form.cleaned_data['linkedin']
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        try:
            redes_empresa = EmpresaRedesSociales.objects.get(empresa_id=representante.empresa.id)
            redes_empresa.fecha_modificacion = datetime.now()
            redes_empresa.usuario_modificacion = persona.usuario.username
        except EmpresaRedesSociales.DoesNotExist:
            redes_empresa = EmpresaRedesSociales()
            redes_empresa.fecha_creacion = datetime.now()
            redes_empresa.usuario_creacion = persona.usuario.username
            redes_empresa.empresa = representante.empresa
        redes_empresa.facebook = facebook
        redes_empresa.twitter= twitter
        redes_empresa.linkedin = linkedin
        redes_empresa.estado = 'A'
        redes_empresa.save()

        return super(RedesSocialesView, self).form_valid(form)

class LogoView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    form_class = forms.LogoForm
    template_name = 'empresa/mi-empresa-logo.html'
    success_url = reverse_lazy('mi-empresa')

    def get_object(self, queryset=None):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        return empresa

class UbicacionView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    form_class = forms.UbicacionForm
    template_name = 'empresa/mi-empresa-ubicacion.html'
    success_url = reverse_lazy('mi-empresa')

    def get_object(self, queryset=None):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante =  get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        return empresa

class OportunidadListarView(TemplateView):
    template_name = 'empresa/oportunidad-listar.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        oportunidades =  Oportunidad.objects.filter(empresa_id = empresa.id).order_by("-fecha_publicacion")
        context = super(OportunidadListarView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidades'] = oportunidades
        return context

################################################# PRUEBAS
class OportunidadBusquedaView(TemplateView):
    def get(self, request, *args, **kwargs):
        # busqueda = request.GET['busqueda']
        busqueda = 'A'
        oportunidades = Oportunidad.objects.filter(Q(estado__icontains=busqueda))
        a_empresas =[]
        # for i in range(0, len(empresas)):
        #     sector = empresas[i].nombre
        #     if empresas[i].sector is not None:
        #         sector = Sector.objects.get(id=empresas[i].sector.id).descripcion
        #     e = {
        #         "id": empresas[i].id,
        #         "nombre": empresas[i].nombre,
        #         "logo": empresas[i].set_logo,
        #         "sector": sector,
        #         "ranking_general": empresas[i].ranking_general,
        #     }
        #     a_empresas.append(e)
        data = serializers.serialize('json', oportunidades,
                                     fields=('id','empresa', 'titulo', 'fecha_cese' ))
        # data = json.dumps(a_empresas)
        #data = json.dumps(oportunidades)
        return HttpResponse(data, content_type='application/json')

def oportunidades(request):
    oportunidades = Oportunidad.objects.all().order_by('-fecha_publicacion')
    a_oportunidades =[]
    for i in range(0, len(oportunidades)):
        empresa = Empresa.objects.get(id=oportunidades[i].empresa.id)
        ciudad = empresa.ciudad
        pais = empresa.pais
        e = {
            "id": oportunidades[i].id,
            "titulo": oportunidades[i].titulo,
            "empresa": empresa.nombre,
            "logo": empresa.set_logo,
            "ubicacion": str(ciudad) + ', ' +str(pais),
            "fecha_cese": str(oportunidades[i].fecha_cese),
            "remuneracion": str(oportunidades[i].remuneracion),
        }
        a_oportunidades.append(e)
    paginator = Paginator(oportunidades, 5)
    if request.method == 'GET':
        if request.is_ajax():
            if request.GET.get('callback'):
                # Paginate based on the page number in the GET request
                page_number = request.GET.get('callback');
                try:
                    page_objects = paginator.page(page_number)
                except InvalidPage:
                    return HttpResponse({'end':'end'},content_type="json")
                # Serialize the paginated objects
                data = serializers.serialize("json", page_objects)
                return HttpResponse(data, content_type='application/json')
    oportunidades = paginator.page(1)
    data = serializers.serialize("json", oportunidades)
    return HttpResponse(data, content_type='application/json')

def oportunidades_listar( request ):
    user = request.user
    persona = get_object_or_404(Persona, usuario_id=user.id)
    representante = get_object_or_404(Representante, persona_id =persona.id)
    return render_to_response('empresa/oportunidad-lista.html', context_instance=RequestContext(request))

def oportunidad_busqueda(request):
    if request.is_ajax():
        busqueda = request.GET.get('b')
        user = request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        if busqueda is not None:
            oportunidades = Oportunidad.objects.filter(estado_oportunidad = busqueda, empresa_id= empresa.id).order_by("-fecha_publicacion")
        else:
            oportunidades = Oportunidad.objects.filter(estado_oportunidad = 'A', empresa_id= empresa.id)
        return render_to_response('empresa/oportunidades.html', {'oportunidades': oportunidades, 'empresa': empresa},
                                  context_instance = RequestContext(request))

##################################################PRUEBAS

class OportunidadBuscarView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        busqueda = request.GET.get('b')
        user = request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        if busqueda is not None:
            oportunidades = Oportunidad.objects.filter(estado_oportunidad = busqueda, empresa_id= empresa.id).order_by("-fecha_publicacion")
        else:
            oportunidades = Oportunidad.objects.filter(estado_oportunidad = 'A', empresa_id= empresa.id)
        list_op =[]
        for op in oportunidades:
            e = {
                "id": op.id
            }
            list_op.append(e)
        data = json.dumps(list_op)
        # data = serializers.serialize('json', oportunidades, fields=('id', 'titulo', 'fecha_cese'))
        return HttpResponse(data, content_type='application/json')

def oportunidad_cargar_lista(request):

    id = request.GET.get('id')
    oportunidad = get_object_or_404(Oportunidad, id = id)
    return render_to_response('empresa/oportunidad-cargar-lista.html', {'oportunidad': oportunidad},
                              context_instance = RequestContext(request))

class OportunidadPostulacionesView(TemplateView):
    def get(self, request, *args, **kwargs):
        id = request.GET['id']
        p = utils.obtener_ultimas_postulaciones(id)
        c = Postulacion.objects.filter(oportunidad_id = id, estado= 'A').count()
        data = []
        data.append((c, p))
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json')

class OportunidadEstudiantes(TemplateView):
    def get(self, request, *args, **kwargs):
        id = request.GET['id']
        estudiante = []
        for p in Postulacion.objects.filter(oportunidad_id=id, estado= 'A').order_by("fecha_creacion")[:6]:
            estudiante.append((p.estudiante.set_foto, p.estudiante.persona.usuario.first_name + " " + p.estudiante.persona.usuario.last_name))

        # data = serializers.serialize('json', oportunidad,
        #                              fields=('id','nombre', 'sector', 'logo', 'ranking_general' ))
        data = json.dumps(estudiante)
        return HttpResponse(data, content_type='application/json')

class OportunidadCandidatos(TemplateView):
    template_name = 'empresa/oportunidad-candidatos.html'

    def get_context_data(self, **kwargs):
        id = kwargs.get('id', None)
        oportunidad =  get_object_or_404(Oportunidad, pk = id)
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        postulaciones = Postulacion.objects.filter(oportunidad_id = id, estado = 'A').count()
        context = super(OportunidadCandidatos, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidad'] = oportunidad
        context['postulaciones'] = postulaciones
        return context

class OportunidadCandidatosCV(TemplateView):
    template_name = 'empresa/oportunidad-candidatos-cv.html'

    def get_context_data(self, **kwargs):
        id_oportunidad = kwargs.get('id', None)
        id_estudiante = kwargs.get('e', None)
        oportunidad =  get_object_or_404(Oportunidad, pk = id_oportunidad)
        estudiante = get_object_or_404(Estudiante, pk = id_estudiante)
        context = super(OportunidadCandidatosCV, self).get_context_data(**kwargs)

        conocimientos_extras = ConocimientoExtra.objects.filter(estudiante_id = estudiante.id)

        fecha_nac = estudiante.persona.fecha_nacimiento

        edad = calular_edad(fecha_nac)

        context['edad'] = edad
        context['oportunidad'] = oportunidad
        context['estudiante'] = estudiante
        context['resumen'] = Resumen.objects.get(estudiante_id=estudiante.id)
        context['actividades_extra'] = ActividadesExtra.objects.filter(estudiante_id=estudiante.id)
        context['experiencias_profesionales'] = ExperienciaProfesional.objects.filter(estudiante_id=estudiante.id)
        context['voluntariados'] = Voluntariado.objects.filter(estudiante_id=estudiante.id)
        context['conocimientos_extras'] = conocimientos_extras
        return context

#
# def datatables_view(request):
#     objects = .objects.all()
#     list_display = ['field1', 'field2', ...]
#     list_filter = [f.name for f in MyModel._meta.fields if isinstance(f, CharField)]
#     #a simple way to bring all CharFields, can be defined in specifics
#
#     # count total items:
#     iTotalRecords = objects.count()
#
#     #filter on list_filter using __contains
#     search = request.GET['sSearch']
#     queries = [Q(**{f+'__contains' : search}) for f in list_filter]
#     qs = reduce(lambda x, y: x|y, queries)
#     objects = objects.filter(qs)
#
#     #sorting
#     order = dict( enumerate(list_display) )
#     dirs = {'asc': '', 'desc': '-'}
#     ordering = dirs[request.GET['sSortDir_0']] + order[int(request.GET['iSortCol_0'])]
#     objects = objects.order_by(order_by)
#
#     # count items after filtering:
#     iTotalDisplayRecords = objects.count()
#
#
#     # finally, slice according to length sent by dataTables:
#     start = int(request.GET['iDisplayStart'])
#     length = int(request.GET['iDisplayLength'])
#     objects = objects[ start : (start+length)]
#
#     # extract information
#     data = [map(lambda field: getattr(obj, field), list_display) for obj in objects]
#
#     #define response
#     response = {
#         'aaData': data,
#         'iTotalRecords': iTotalRecords,
#         'iTotalDisplayRecords': iTotalDisplayRecords,
#         'sEcho': request.GET['sEcho']
#     }
#
#     #serialize to json
#     s = StringIO()
#     json.dump(response, s)
#     s.seek(0)
#     return HttpResponse(s.read())

class PictureCreateView(CreateView):
    model = Picture
    fields = "__all__"

    def get_initial(self):
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        return {
            'empresa':empresa,
        }

    def form_valid(self, form):
        persona = Persona.objects.get(usuario_id= self.request.user)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        form.instance.empresa = empresa
        self.object = form.save()
        self.empresa = empresa
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')

class PictureDeleteView(DeleteView):
    model = Picture

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

class PictureListView(ListView):
    model = Picture

    def get_queryset(self):
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        pictures = Picture.objects.filter(empresa_id = empresa.id)
        return pictures

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

def video_url_create(request):
    url = request.POST['url']
    try:
        representante = get_object_or_404(Representante, persona__usuario = request.user.id)
        empresa = Empresa.objects.get(id = representante.empresa.id)
        video_url = VideoUrl()
        video_url.empresa = empresa
        video_url.url = url
        video_url.save()
        data = video_url.id
    except Exception:
        data = "-1"

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

def video_url_delete(request):
    id = request.POST['id']
    user = request.user
    persona = Persona.objects.get(usuario_id=user.id)
    representante = get_object_or_404(Representante, persona_id =persona.id)
    try:
        video_url = VideoUrl.objects.get(id = id).delete()
        data = "0"
    except Exception:
        data = "-1"

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

def video_url_list(request):
    videos = VideoUrl.objects.filter()
    data = serializers.serialize('json', videos,
                                     fields=('id','url'))
    return HttpResponse(data, content_type='application/json')

class VideosListView(TemplateView):
    template_name = 'empresa/video_form.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = get_object_or_404(Persona, usuario_id=user.id)
        representante = get_object_or_404(Representante, persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        videos = VideoUrl.objects.filter(empresa_id = empresa.id)
        context = super(VideosListView, self).get_context_data(**kwargs)
        context['videos'] = videos
        return context

def empresa_slider_imagenes(request, id):
    # id = request.GET.get('id')
    imagenes = Picture.objects.filter(empresa_id = id)
    videos = VideoUrl.objects.filter(empresa_id = id)
    return render_to_response('empresa/mi-empresa-slider-imagenes.html', {'imagenes': imagenes, 'videos': videos},
                              context_instance = RequestContext(request))

def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    # result = StringIO.StringIO()
    # pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    # if not pdf.err:
    #     return HttpResponse(result.getvalue(), mimetype='application/pdf')
    # return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))
    return HttpResponse('Error al generar el PDF: ')

def canditado_cv_pdf(request):
    # vista de ejemplo con un hipotético modelo Libro

    id_estudiante = request.get('id', None)
    estudiante = get_object_or_404(Estudiante, pk = id_estudiante)
    conocimientos_extras = ConocimientoExtra.objects.filter(estudiante_id = estudiante.id)
    html = render_to_string('candidato_cv_pdf.html', {'pagesize':'A4', 'estudiante':estudiante,
                                               'conocimientos_extras' : conocimientos_extras},
                            context_instance=RequestContext(request))
    return generar_pdf(html)
