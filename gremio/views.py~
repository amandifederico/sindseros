from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.sites.models import get_current_site
from django.shortcuts import render
from django.template.response import TemplateResponse
from gremio.models import *
from gremio.forms import *
from gremio.funciones import *



def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
	
def prueba(request):
	return render_to_response('index2.html',context_instance=RequestContext(request))
	
def contacto(request):
	return render_to_response('contacts.html',context_instance=RequestContext(request))


#-------AFILIADOS-------
@login_required(login_url='/accounts/login/')
def afiliado(request):
	afiliados = Afiliado.objects.all().order_by('apellido')
	titulo = "Listado Afiliados"
	cant = afiliados.count()
	lista = paginar(afiliados,request)
        return render_to_response('afiliados.html',context_instance=RequestContext(request,{'lista':lista,'titulo':titulo,'cant':cant},))

@login_required(login_url='/accounts/login/')
def abmAfiliado(request,idafiliado):
        user = request.user
    	#grupos = get_grupos(user)
    	name = 'Afiliado'
    	accion = ''
    	form_old=''
	if request.POST:
		if int(idafiliado) >0:
			afil = Afiliado.objects.get(pk=idafiliado)
			form_old = formAfiliado(instance=afil)
			#form_old = modeloLista(form_old.Meta.model.objects.filter(pk=form_old.instance.pk).values_list())
			form = formAfiliado(request.POST, instance=afil)
			accion = 'Modificacion'
		else:
			form = formAfiliado(request.POST)
	      		accion = 'Alta'
		
		if form.is_valid():
			try:
				aux = Afiliado.objects.get(documento=form.instance.documento)
				accion = "Modificacion"
			except Afiliado.DoesNotExist:
				accion = "Alta"
				#if ("Datos Afiliado" not in get_grupos(user)):
				if True:
					form.save()
				#data = unicode(value)
	      
				if accion == "Alta":
					#registrar(user, name, "Alta", getTime(), None, modeloLista(form.Meta.model.objects.filter(pk=form.instance.pk).values_list()))
					pass
				elif accion == "Modificacion":
					#registrar(user,name,"Modificacion",getTime(),form_old,modeloLista(form.Meta.model.objects.filter(pk=form.instance.pk).values_list()))
					if int(idagente) != 0:
						#url = '/personal/forms/menuagente?idagente='+str(idagente)
						url = '/index'
					else:
						#url = '/personal/listado/agentes?opc=2'
						url = '/index'
					return HttpResponseRedirect(url)
	else:
		if int(idafiliado) >0:
			##MODIFICACION
			a = Afiliado.objects.get(pk=idafiliado)
			form = formAfiliado(instance=a)
		else:
			##ALTA
			form = formAfiliado()

	return render_to_response('forms/abm.html',context_instance=RequestContext(request, {'form': form}))


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
