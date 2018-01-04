from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
def pg_records(request, list, num):
    print(request)
    #print(num)
    print (list)
    paginator = Paginator(Inscripcion.objects.all(), 2)
    print (paginator)

    # get the page parameter from the query string
    # if page parameter is available get() method will return empty string ''
    page = request.GET.get('page')

    try:
        # create Page object for the given page
        page_object = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        page_object = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        page_object = paginator.page(paginator.num_pages)

    return page_object