#coding:utf-8
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect,Http404  
def index(request):
    login_flag = False
    kola_name = ''
    if "login_flag" in request.session:
        login_flag = True
        kola_name = request.session['name']
    return render(request,'text_index.html',locals())
