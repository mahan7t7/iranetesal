from django.urls import path , include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index_view , name='index'),
    path('about/', views.about_view , name='about'),
    path('store/', views.store_view , name='store'),
    path('search/', views.search_view , name='search'),
    path('logout/', views.logout_view , name='logout'),
    path('<int:id>',views.delete_one_purchase , name='del'),
    path('del-cart/',views.delete_cart, name='del-cart'),
    path('dashboard/', views.profile_view , name='profile'),
    path('news/', views.news_view , name='news'),
    path('<int:id>', views.news_detail_view, name='newsdetail'),
    path('purchase-success/', views.finished_purchase , name='sold'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        #views.activate, name='activate'),
]
