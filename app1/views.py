
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Setsession(request):
    request.session['sname']='shubham'
    request.session['email']='sp3336705@gmail.com'
    return HttpResponse('session is set')
def get_session(request):
    StudentName=request.session['sname']
    Student_Email=request.session['email']
    return HttpResponse(StudentName+" "+ Student_Email)
    
    
# delete session
def delitem(request):
    del request.session['sname']
    return HttpResponse('session deleted')    
def setcookies(request):
    response=HttpResponse('cookie set successfully')
    response.set_cookie("javapoint",'python')
    return response
def getcookie(request):
    tutorial=request.COOKIES('javapoint')
    return HttpResponse('javapoint tutorial@',tutorial)