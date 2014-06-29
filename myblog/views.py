#coding:utf-8
from django.shortcuts import render_to_response,render,get_object_or_404  
from django.http import HttpResponse, HttpResponseRedirect,Http404  
from myblog.models import *
from django.core.mail import send_mail
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

import PyEmail
import settings
import geetest
#import sae
#from PIL import Image

def index(request):
    '''
    首页
    '''
    return render(request,'index.html')

def blog(request):
    '''
    博客主页
    '''
    mess = []  
    #try:
    messages_list = Kola_message.objects.order_by('-pub_date')[:10]
    blog_list = MyBlog.objects.order_by('-pub_date')

    #总数据列表
    paginator = Paginator(blog_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    for i in messages_list:
        #留言板的标题和简介
        if len(i.text)>200:
            mess.append(i.text[:200]+'[...]')
        else:
            mess.append(i.text)
    messages = zip(messages_list,mess) 
    return render(request,'blog.html',locals())

def detail(request,blog_id):
    '''
    详细博文内容
    '''
    try:
        blog = MyBlog.objects.get(pk=blog_id)
    except MyBlog.DoesNotExist:
        raise Http404
    return render(request,'detail.html',locals())

def post_message(request,blog_id):
    '''
    博客留言
    '''
    errors=[]
    flag = ""
    if request.method == "POST":
        if not request.POST.get('message',''):
            errors.append(u'请输入留言内容')
        if not errors:
            mes =Message(
                name=request.POST.get('name',''),
                email= request.POST.get('email',''),
                text= request.POST.get('message',''),
                blog_id=blog_id,
                )
            mes.save()
            flag = u"评论成功。"
    return render_to_response('detail.html',
        locals(),
        context_instance=RequestContext(request))

def post_a_message(request):
    '''
    留言板留言
    '''
    errors=[]
    flag = ""
    if request.method == "POST":
        if not request.POST.get('message',''):
            errors.append(u'请输入留言内容')
        if not errors:
            mes =Kola_message(
                name=request.POST.get('name',''),
                email= request.POST.get('email',''),
                text= request.POST.get('message',''),
                )
            mes.save()
            flag = u"留言成功提交。"
            try:
                title = "message:"+request.POST.get('name','').encode('utf-8')+';'+request.POST.get('email','').encode('utf-8')
                content = request.POST.get('message','').encode('utf-8')
                PyEmail.SendMail('kola@bigkola.info',title,content) 
            except:
                pass

    return HttpResponseRedirect("/message/")

def bigkola(request):
    '''
    联系bigkola
    '''
    return render(request,'bigkola.html')

def message(request):
    '''
    留言板
    '''
    mes = Kola_message.objects.order_by('-pub_date')[:100]
    errors=[]
    flag = ""
    if request.method == "POST":
        #验证部分代码 +++++++++++++++++++++++++++++++++++++++++++++++
        challenge = request.POST.get('geetest_challenge')
        validate = request.POST.get('geetest_validate')
        seccode = request.POST.get('geetest_seccode')
        gt = geetest.geetest('geetest_KEY')
        if not gt.geetest_validate(challenge, validate, seccode):
            errors.append(u'验证未通过，请先通过验证')       
        #  ——————————————————————————————————————————————————————————
            
        if not request.POST.get('message',''):
            errors.append(u'请输入留言内容')
        if not errors:
            message =Kola_message(
                name=request.POST.get('name',''),
                email= request.POST.get('email',''),
                text= request.POST.get('message',''),
                )
            message.save()
            flag = u"留言成功提交。"
            try:
                title = "message:"+request.POST.get('name','').encode('utf-8')+';'+request.POST.get('email','').encode('utf-8')
                content = request.POST.get('message','').encode('utf-8')
                PyEmail.SendMail('kola@bigkola.info',title,content) 
            except:
                pass
    return render(request,'message.html',locals())

def empire(request):
    return  HttpResponse(u'暂未开通....')

def history(request):
    '''
    编年史板块
    '''
    return render(request,'history.html')

def wiki(request):
    '''
    百科全书板块
    '''
    return render(request,'wiki.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append(u'请填写查询内容！')
        elif len(q)>20:
            errors.append(u'填写内容必须小于20字！')
        else:  
            blog = MyBlog.objects.filter(title__icontains=q)
            return render_to_response('search.html',
                {'blog':blog,'q':q},context_instance=RequestContext(request))
    return render_to_response('search.html',{'errors':errors},
        context_instance=RequestContext(request))

def email(request):
    errors=[]
    flag = ""
    if request.method == "POST":
        if not request.POST.get('name',''):
            errors.append(u'请输入你的名字')
        if not request.POST.get('email',''):
            errors.append(u'请输入您的邮箱地址')
        if not request.POST.get('message',''):
            errors.append(u'请输入邮件内容')
        if not errors: 
            try:
                title = 'bigkola'+':'+request.POST.get('name','').encode('utf-8') +';'+request.POST.get('email','').encode('utf-8')
                content = request.POST.get('message','').encode('utf-8')
                PyEmail.SendMail('kola@bigkola.info',title,content)         
                flag = u"邮件发送成功。"
            except:
                flag =u'邮件发送失败'
    return render_to_response('email.html',locals(),context_instance=RequestContext(request))


def test(request):
    pass

#登录视图:
#@csrf_exempt
def login(request):
    errors = []
    register_flag = False
    if request.method == "POST":
        if not request.POST.get('username',''):
            errors.append(u"请输入用户名")
        if not request.POST.get('password',''):
            errors.append(u"请输入密码")
        else:
            name = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=name,
                password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect("/index/")
            else:
                errors.append(u'登录失败，请重试')
    #response = render(request,'login.html',locals())
    response = render_to_response('login.html',
        {'errors':errors,},
        context_instance=RequestContext(request))
    return render(request,'login.html',locals())

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return render(request,"logout.html",{})
    else:
#        return render(request,"logout.html",{})
        return HttpResponseRedirect("/index/") 



#注册视图
from django.contrib.auth.models import User

@csrf_exempt
def register(request):
    errors=[]
    if request.method == 'POST':
        name = request.POST.get('username','')
        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2','')
        if len(name)<3:
            errors.append(u'用户名长度必须大于4个字符')
        elif len(password1)<6:
            errors.append(u'密码长度必须大于6个字符')
        elif password1 != password2 :
            errors.append(u'两次输入密码必须相同')
        else:
            try:
                user = User.objects.get(username=name)
                errors.append(u'用户名已被注册')
                return render(request,'register.html',{'errors':errors})
            except User.DoesNotExist:    
                user = User.objects.create_user(
                    username = name,
                    password = password1,
                    )
                register_flag = True
                return render(request,'login.html',{'register_flag':register_flag})
        return render(request,'register.html',{'errors':errors})
    else:
        return render(request,'register.html')
