from django.shortcuts import render , redirect , get_object_or_404
from itertools import chain
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required
from accounts.models import User as User, UserManager
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_out
from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import send_mass_mail
from .backends import TOTPVerification
from unittest import mock
import requests
import time

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
import xlwt



from zanoei.models import Elbow
from cap.models import Cap
from nippel.models import Nippel
from reducer.models import Reducer
from tee.models import Tee
from purchase.models import Purchase
from purchase.forms import PurchaseForm
from news.models import News
from sold.models import Sold , SoldManager
# Create your views here.

def index_view(request):
    elbow = Elbow.objects.get(pk=1)
    context = { 'elbow': elbow}

    # Register
    if request.method == 'POST':
        if 'first_name' and 'last_name' and 'email' and 'phone' and 'rpassword' in request.POST:
            if request.POST['first_name'] and request.POST['last_name'] and request.POST['email'] and request.POST['phone'] and request.POST['rpassword']:
                try:
                    if User.objects.filter(email = request.POST['email']) :
                        messages.warning(request, 'این ایمیل قبلا استفاده شده است')
                        return render(request , 'pages/index.html' , context)
                except ObjectDoesNotExist:
                    raise
                try:
                    if User.objects.filter(phone = request.POST['phone']) : 
                        messages.warning(request, 'این شماره همراه قبلا استفاده شده است')
                        return render(request , 'pages/index.html' , context)   
                except ObjectDoesNotExist:
                    raise        

                request.session["first_name"]    = request.POST['first_name']
                request.session["last_name"]     = request.POST['last_name']
                request.session["company_name"]  = request.POST['company_name']
                request.session["email"]         = request.POST['email']
                request.session["phone"]         = request.POST['phone']
                request.session["password"]      = request.POST['rpassword']

                request.session["inlineRadioOptions"] = request.POST['inlineRadioOptions']
                verify = request.session["inlineRadioOptions"]
                totpv = TOTPVerification()
                generated_token = totpv.generate_token()
                request.session["generated_token"] =  generated_token
                phone = request.session["phone"]
                email = request.session["email"]
                first_name = request.session["first_name"]
                if verify == "option2":
                    message2 = ('Iran Etesal', 'Dear '+ first_name+'\nYour confirmation code is: '+ generated_token , 'enigma7t7@gmail.com', [email])
                    send_mass_mail((message2, ), fail_silently=False)
                else:
                    url = "https://api.ghasedak.io/v2/sms/send/simple"
                    payload = {'message':'your activation code is: '+ generated_token , 'receptor' : phone, 'linenumber': '30005006004963', 'senddate': '', 'checkid': ''}
                    headers = {
                        'apikey': "e64d32090d1ac50b358684636f4bdf286a70fe8ac30cb12f7a0e2b4a4ba81d3f",
                        }

                    response = requests.post(url, data=payload, headers=headers)
                    sms = response.text

                context = { 'elbow': elbow}
                return render(request , 'pages/verification.html' , context)

            else:
                print("incomplete info")
        else:
            print("incomplete info")
    # Confirm Register
    if request.method == 'POST':
        if 'confirm_code'  in request.POST:
            if request.POST['confirm_code']:
                first_name       = request.session["first_name"]
                last_name        = request.session["last_name"]
                company_name     = request.session["company_name"]
                email            = request.session["email"]
                phone            = request.session["phone"]
                password         = request.session["password"]


                token = request.POST['confirm_code']
                generated_token = request.session["generated_token"]
                if token==generated_token:
                    User.objects.create_user_complete(first_name, last_name, company_name, phone, email, password)
                    user = authenticate(username = email, password = password)
                    login(request, user)
                else:
                    messages.warning(request , 'اطلاعات وارد شده صحیح نیست')    
            else:
                messages.warning(request , 'اطلاعات وارد شده صحیح نیست')
      #  else:
       #     messages.warning(request , 'اطلاعات وارد شده صحیح نیست')

            return render(request , 'pages/index.html' , context)    
            
        
      
    #     #UserManager.create_user_complete( first_name, last_name, company_name , username, password)
        

     #Login
    if request.method == 'POST':
        if 'username' and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            context = { 'elbow':elbow }
            if username is not None and password is not None:
                try:
                    user = authenticate(username = username, password = password)
                except:
                     messages.warning(request, 'Invalid Input')
                     return render(request, 'pages/index.html', context)
                if user is not None:
                    try:
                        login(request, user)
                        messages.success(request, 'شما با موفقیت وارد حساب کاربری خود شدید')
                    except:
                        messages.warning(request, 'Invalid Input')
                        return render(request, 'pages/index.html',context)
                else:
                    messages.warning(request , 'اطلاعات وارد شده صحیح نیست')
                    return render(request, 'pages/index.html', context)
            else:
                messages.warning(request , 'اطلاعات وارد شده صحیح نیست')
                return render(request, 'pages/index.html', context)
        else:
            messages.warning(request , 'اطلاعات وارد شده صحیح نیست')        
            return render(request, 'pages/index.html', context) 
    context = { 'elbow': elbow}
    return render(request , 'pages/index.html' , context)

    #if request.user.is_authenticated:
     #   purchased = Purchase.objects.filter(user=request.user)
      #  summ = 0
       # for item in purchased:
        #    summ += item.price 
        
        #context = {
        #    'purchased': purchased ,
        #    'summ': summ,
         #   'elbow': elbow
        #    }   
    #else:
     #   context = { 'elbow': elbow}
   # return render(request , 'pages/index.html' , context)

#def activate(request, uidb64, token , backend='django.contrib.auth.backends.ModelBackend'):
    #try:
     #   uid = force_text(urlsafe_base64_decode(uidb64))
      #  user = User.objects.get(pk=uid)
   # except(TypeError, ValueError, OverflowError, User.DoesNotExist):
      #  user = None
   # if user is not None and account_activation_token.check_token(user, token):
     #   user.active = True
     #   user.save()
     #   login(request, user , backend='django.contrib.auth.backends.ModelBackend')
      #  return redirect('index')
      #  messages.success(request, 'تایید حساب کاربری شما با موفقیت انجام شد')
   # else:
        #messages.error(request, 'لینک تایید حساب کاربری صحیح نمی باشد')


def about_view(request):
    return render(request , 'pages/about.html')
    
def store_view(request):
    elbow = Elbow.objects.filter(id=1)
    cap = Cap.objects.filter(id=1)
    nippel = Nippel.objects.filter(id=1)
    reducer = Reducer.objects.filter(id=3)
    tee = Tee.objects.filter(id=3)
    queryset = []
    queryset.append(elbow)
    queryset.append(nippel)
    queryset.append(reducer)
    queryset.append(cap)
    queryset.append(tee)

    context = {
        'items': queryset
    }
    return render(request , 'pages/store.html', context)



def logout_view(request):
    logout(request)
    print("AAAA")
    return redirect('index')


def search_view(request):
    elbow_queryset   = Elbow.objects.all()
    tee_queryset     = Tee.objects.all()
    reducer_queryset = Reducer.objects.all()
    nippel_queryset  = Nippel.objects.all()
    cap_queryset     = Cap.objects.all()
    queryset_list = list(chain(elbow_queryset, tee_queryset, reducer_queryset, nippel_queryset, cap_queryset))
    

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            elbow_queryset = elbow_queryset.filter(Q(name__icontains=keywords) | Q(مدل__icontains=keywords))
            tee_queryset = tee_queryset.filter(Q(name__icontains=keywords) | Q(مدل__icontains=keywords))
            reducer_queryset = reducer_queryset.filter(Q(name__icontains=keywords) | Q(مدل__icontains=keywords))
            nippel_queryset = nippel_queryset.filter(Q(name__icontains=keywords) | Q(مدل__icontains=keywords))
            cap_queryset = cap_queryset.filter(Q(name__icontains=keywords) | Q(مدل__icontains=keywords))
            queryset_list = list(chain(elbow_queryset, tee_queryset, reducer_queryset, nippel_queryset, cap_queryset))

    # Name
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            elbow_queryset = elbow_queryset.filter(name__icontains=name)
            tee_queryset = tee_queryset.filter(name__icontains=name)
            reducer_queryset = reducer_queryset.filter(name__icontains=name)
            nippel_queryset = nippel_queryset.filter(name__icontains=name)
            cap_queryset = cap_queryset.filter(name__icontains=name)
            queryset_list = list(chain(elbow_queryset, tee_queryset, reducer_queryset, nippel_queryset, cap_queryset))

    # model
    if 'مدل' in request.GET:
        مدل = request.GET['مدل']
        if مدل:
            elbow_queryset = elbow_queryset.filter(مدل__icontains=مدل)
            tee_queryset = tee_queryset.filter(مدل__icontains=مدل)
            reducer_queryset = reducer_queryset.filter(مدل__icontains=مدل)
            nippel_queryset = nippel_queryset.filter(مدل__icontains=مدل)
            cap_queryset = cap_queryset.filter(مدل__icontains=مدل)
            queryset_list = list(chain(elbow_queryset, tee_queryset, reducer_queryset, nippel_queryset, cap_queryset))

    

    if request.user.is_authenticated:
        form = PurchaseForm (request.POST , instance=Purchase(user=request.user))
        if form.is_valid():
            form.save()
            print("purchase saved")
        else:
            print("not valid") 

        purchased = Purchase.objects.filter(user=request.user)
        summ = 0
        for item in purchased:
            summ += item.price 
    
        context = {
            'products': queryset_list , 
            'form': form ,
            'purchased': purchased ,
            'summ': summ
        }   
    else:
        context = {
            'products': queryset_list , 
        }           
    return render(request, 'pages/search.html' , context)

def profile_view(request):
    purchased = Purchase.objects.filter(user=request.user)
    summ = 0
    for item in purchased:
        summ += item.price 
    context = {
        'purchased':purchased,
        'summ':summ
    }
    return render(request , 'pages/dashboard.html', context)

def news_view (request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request , 'pages/news.html', context)


def news_detail_view (request , id):
    news = get_object_or_404(News, pk=id)
    context = {
        'news':news
    }
    return render(request, 'pages/news_open.html', context)
def delete_one_purchase(request , id):
    Purchase.objects.filter(id=id).delete() 
    return redirect(search_view)
def delete_cart(request):
    delete_purchase(request.user)
    return redirect(search_view)

def delete_purchase(user):
    purchase = Purchase.objects.filter(user=user)
    purchase.delete()

def on_logout(sender, **kwargs):
    if kwargs['user']:
        delete_purchase(kwargs['user'])

user_logged_out.connect(on_logout, dispatch_uid="user_logout1")

def finished_purchase(request):
    purchased = Purchase.objects.filter(user=request.user)
    for item in purchased:
        item.purchased = True
        if item.purchased:
            Sold.objects.validate_sold(item.user , item.name , item.model , item.size , item.number , item.price)
    messages.success(request, "خرید شما با موفقیت انجام شد")
    return redirect(index_view)
