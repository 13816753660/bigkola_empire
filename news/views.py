#coding:utf-8
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect,Http404  
from news.models import News,NewsTag
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import random
def index(request):
    login_flag = False
    kola_name = ''
    errors = []
    flag = ''
    news_list = []
    if "login_flag" in request.session:
        login_flag = True
        kola_name = request.session['name']
    news = News.objects.order_by("-dt")
    if request.method == "POST":
        if len(request.POST.get('news',''))<70:
            errors.append(u'提交内容长度必须大于70字.')
        if len(request.POST.get('news',''))>1000:
            errors.append(u"提交内容长度过长,不超过1000个字.")
        if not errors:
            new_news =News(
                text=request.POST.get('news',''),
                source=u"匿名新闻",
                )
            new_news.save()
            request.session["news_flag"] = True
            flag = u"匿名新闻提交成功。"
            return HttpResponseRedirect('/news/')

    paginator = Paginator(news, 40) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)    
    return render(request,'news_index.html',locals())


def detail(request):
    #news = News.objects.get(pk=news_id)
    return HttpResponse("ok")
    #return render(request,'news',locals())

def news_detail(request,news_id):
    news = News.objects.get(pk=news_id)
    return render(request,'news.txt',locals())