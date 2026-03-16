from django.http import HttpResponse

def handler400(request, exception):
    return HttpResponse('400: Bad request!', status=400)


def handler403(request, exception):
    return HttpResponse('403: Permission denied!', status=403)


def handler404(request, exception):
    return HttpResponse('404: Page not found!', status=404)


def handler500(request):
    # note: no `exception` argument for 500
    return HttpResponse('500: Internal server error!', status=500)