from django.shortcuts import render , redirect , get_object_or_404
from itertools import chain
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required
from accounts.models import User as User, UserManager
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_out

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

    # Register
    if request.method == 'POST':
        if 'first_name' and 'last_name' and 'email' and 'phone' and 'rpassword' in request.POST:
            if request.POST['first_name'] and request.POST['last_name'] and request.POST['email'] and request.POST['phone'] and request.POST['rpassword']:
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                company_name = request.POST['company_name']
                email = request.POST['email']
                phone = request.POST['phone']
                password = request.POST['rpassword']
                user = User.objects.create_user_complete(first_name, last_name, company_name, phone, email, password)
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('acc_active_email.html', {
                    'user':user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                    })
                to_email = user.email
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                try:
                    email.send()
                except:
                    messages.warning(request , 'ایمیل وارد شده صحیح نیست')
            else: 
                messages.warning(request , 'اطلاعات وارد شده صحیح نیست')
            
            
        
      
    #     #UserManager.create_user_complete( first_name, last_name, company_name , username, password)
        

     #Login
    if request.method == 'POST':
        if 'username' and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            if username is not None and password is not None:
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'شما با موفقیت وارد حساب کاربری خود شدید')

    if request.user.is_authenticated:
        purchased = Purchase.objects.filter(user=request.user)
        summ = 0
        for item in purchased:
            summ += item.price 
        
        context = {
            'purchased': purchased ,
            'summ': summ,
            'elbow': elbow
            }   
    else:
        context = { 'elbow': elbow}
    return render(request , 'pages/index.html' , context)

def activate(request, uidb64, token , backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.active = True
        user.save()
        login(request, user , backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
        messages.success(request, 'تایید حساب کاربری شما با موفقیت انجام شد')
    else:
        messages.error(request, 'لینک تایید حساب کاربری صحیح نمی باشد')


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