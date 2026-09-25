from django.shortcuts import render

#function for 400 error
def error_400(request, exception):
    context = {'exception': exception}
    response = render(request, 'error/400.html', context = context)
    response.status_code = 400
    return response
# function for 403 error
def error_403(request, exception):
    context = {'exception': exception}
    response = render(request, 'error/403.html', context = context)
    response.status_code = 403
    return response
#function for 404 error
def error_404(request, exception):
    context = {'exception': exception}
    response = render(request, 'error/404.html', context = context)
    response.status_code = 404
    return response
#function for 500 error
def error_500(request):
    response = render(request, 'error/500.html')
    response.status_code = 500
    return response