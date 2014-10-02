from django.core.paginator import Paginator, InvalidPage, EmptyPage

def paginar(objlist,peticion):
    """Metodo que pagina el resultado de un reporte de tipo listado """
    cant = 40 #cantidad por pagina
    paginator = Paginator(objlist,cant)
    try:
        page = int(peticion.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        lista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista = paginator.page(paginator.num_pages)
    return lista
