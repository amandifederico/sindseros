from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.sites.models import get_current_site
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from gremio.models import *

def paginar(objlist,peticion):
    paginator = Paginator(objlist,40)
    
    try:
        page = int(peticion.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        lista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista = paginator.page(paginator.num_pages)
    return lista


def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
	
def prueba(request):
	return render_to_response('index2.html',context_instance=RequestContext(request))
	
def contacto(request):
	return render_to_response('contacts.html',context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def afiliado(request):
	afiliados = Afiliado.objects.all().order_by('apellido')
	titulo = "Listado Afiliados"
	cant = afiliados.count()
	afi = paginar(afiliados,request)
        return render_to_response('afiliados.html',context_instance=RequestContext(request,{'afi':afi,'titulo':titulo,'cant':cant},))

#////////////////////////////////////////////////////////////////////////////////////////
def logout(request, next_page=None,
           template_name='registration/logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           current_app=None, extra_context=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    if redirect_to:
        netloc = urlparse.urlparse(redirect_to)[1]
        # Security check -- don't allow redirection to a different host.
        if not (netloc and netloc != request.get_host()):
            return HttpResponseRedirect(redirect_to)

    if next_page is None:
        current_site = 'index'
        context = {
            'site': 'index',
            'site_name': 'Inicio',
            'title': 'Usted esta saliendo...'
        }
        if extra_context is not None:
            context.update(extra_context)
        return TemplateResponse(request, template_name, context,
                                current_app=current_app)
    else:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page or request.path)
