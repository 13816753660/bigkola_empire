#coding:utf-8
# Create your views here.
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect,Http404 
from worldcup2014.models import Team1,Game,GameDate,Team2,Menu

teams=u'''澳大利亚,伊朗,日本,韩国,阿尔及利亚,喀麦隆,科特迪瓦,
    加纳,尼日利亚,哥斯达黎加,洪都拉斯,墨西哥,美国,阿根廷,
    巴西,智利,哥伦比亚,厄瓜多尔,乌拉圭,比利时,
    波斯尼亚与赫塞哥维纳,克罗地亚,英格兰,法国,德国,
    希腊,意大利,荷兰,葡萄牙,俄罗斯,西班牙,瑞士'''
team_list = teams.split(",")

def index(request):
    date = GameDate.objects.all()
    menudata = Menu.objects.all()
    return render(request,"worldcup2014.html",locals())
    return HttpResponse("ok")

def add(request):
    try:
        for i in team_list:
            new_team=Team1(
                name = i,
                )
            new_team.save()
        return HttpResponse("oooooook")
    except:
        return HttpResponse("worng")
    return HttpResponse("add")


def index_all(request):
    data = Menu.objects.all()
    return render(request,"worldcup2014_all.html",locals())

def index_game(request,game_flag):
    data = Menu.objects.get(flag=game_flag)
    return render(request,"worldcup2014_game.html",locals())
