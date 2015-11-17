from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy


# Create your views here.
class OportunidadCrearView(FormView):
    form_class = forms.OportunidadCrearForm
    template_name = 'oportunidad/crear.html'
    success_url = reverse_lazy('mi-empresa')

    def form_valid(self, form):

		print("aqui")
		return super(OportunidadCrearView , self).form_valid(form)



