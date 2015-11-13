from django.shortcuts import render

# Create your views here.
@login_required(login_url='/empresa-registro/')
def oportunidad_listar(request):
    return render(request, 'empresa/oportunidad-listar.html')