# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Puesto, Empresa, Representante, Sector
from main.models import Persona, Universidad, Carrera, Pais, Ciudad, TipoPuesto, Idioma
from oportunidad.models import Oportunidad, Postulacion
from estudiante.models import Estudiante
from django.core.paginator import Paginator, InvalidPage
from django.template import RequestContext
from empresa import utils
from django.shortcuts import render, render_to_response, redirect, get_object_or_404

import json

# Create your views here.
@login_required(login_url='/empresa-registro/')
def oportunidad_listar(request):
    return render(request, 'empresa/oportunidades-listar.html')

class MiEmpresaView(FormView):
    form_class = forms.LogoForm
    template_name = 'empresa/mi-empresa.html'
    success_url = reverse_lazy('mi-empresa')

    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        oportunidades =  Oportunidad.objects.filter(empresa_id = empresa.id)[:3]
        context = super(MiEmpresaView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidades'] = oportunidades
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

class InfoGeneralView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):

        form_class = forms.InfoGeneralForm
        template_name = 'empresa/mi-empresa-info-general.html'
        success_url = reverse_lazy('mi-empresa')

        #get object
        def get_object(self, queryset=None):
            user = self.request.user
            persona = Persona.objects.get(usuario_id=user.id)
            representante = Representante.objects.get(persona_id =persona.id)
            empresa = Empresa.objects.get(id=representante.empresa.id)
            return empresa

class LogoView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    form_class = forms.LogoForm
    template_name = 'empresa/mi-empresa-logo.html'
    success_url = reverse_lazy('mi-empresa')

    def get_object(self, queryset=None):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        return empresa

class UbicacionView(SuccessMessageMixin, AjaxTemplateMixin,UpdateView):
    form_class = forms.UbicacionForm
    template_name = 'empresa/mi-empresa-ubicacion.html'
    success_url = reverse_lazy('mi-empresa')

    def get_object(self, queryset=None):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        return empresa

class OportunidadListarView(TemplateView):
    template_name = 'empresa/oportunidad-listar.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        oportunidades =  Oportunidad.objects.filter(empresa_id = empresa.id).order_by("fecha_publicacion")
        context = super(OportunidadListarView, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidades'] = oportunidades
        return context

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

from django.http import HttpResponse
from django.core.paginator import InvalidPage, Paginator

def oportunidades(request):
    oportunidades = Oportunidad.objects.all().order_by('fecha_publicacion')
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

# displays the index page
def oportunidades_listar( request ):
    return render_to_response('empresa/oportunidad-lista.html', context_instance=RequestContext(request))

# search view
def oportunidad_busqueda(request):
    if request.is_ajax():
        busqueda = request.GET.get('b')
        user = request.user
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        if busqueda is not None:
            oportunidades = Oportunidad.objects.filter(estado_oportunidad = busqueda, empresa_id= empresa.id).order_by("fecha_publicacion")
        else:
            oportunidades = Oportunidad.objects.filter(estado_oportunidad = 'A', empresa_id= empresa.id)
        return render_to_response('empresa/oportunidades.html', {'oportunidades': oportunidades, 'empresa': empresa},
                                  context_instance = RequestContext(request))

class OportunidadPostulacionesView(TemplateView):
    def get(self, request, *args, **kwargs):
        id = request.GET['id']
        p = utils.obtener_ultimas_postulaciones(id)
        c = Postulacion.objects.filter(oportunidad_id = id).count()
        data = []
        data.append((c, p))
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json')

class OportunidadEstudiantes(TemplateView):
    def get(self, request, *args, **kwargs):
        id = request.GET['id']
        estudiante = []
        for p in Postulacion.objects.filter(oportunidad_id=id).order_by("fecha_creacion")[:6]:
            estudiante.append((p.estudiante.set_foto))

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
        persona = Persona.objects.get(usuario_id=user.id)
        representante = Representante.objects.get(persona_id =persona.id)
        empresa = Empresa.objects.get(id=representante.empresa.id)
        context = super(OportunidadCandidatos, self).get_context_data(**kwargs)
        context['empresa'] = empresa
        context['oportunidad'] = oportunidad
        return context


from django.http import HttpResponse
from django.db.models import Q, CharField

import json
from cStringIO import StringIO

# def datatables_view(request):
#     objects = MyModel.objects.all()
#     list_display = ['field1', 'field2', ...]
#     list_filter = [f.name for f in MyModel._meta.fields if isinstance(f, CharField)] #a simple way to bring all CharFields, can be defined in specifics
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
