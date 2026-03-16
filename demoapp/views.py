from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    
    response = HttpResponse()
    response.headers['Age'] = 20
    
    msg = f"""<br>
    <br>Path: {path}
    <br>Scheme: {scheme}
    <br>Address: {address}
    <br>Method: {method}
    <br>User agent: {user_agent}
    <br>Path info: {path_info}
    <br>
    <br>Headers: {response.headers}
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def about(request):
    return HttpResponse('About us')

def menu(request):
    return HttpResponse('Menu')

def book(request):
    return HttpResponse('Make a booking')
    
def index(request): 
    return HttpResponse("Hello, world.... This is the index view of Demoapp.") 