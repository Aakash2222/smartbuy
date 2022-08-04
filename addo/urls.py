from unicodedata import name
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm

urlpatterns = [

    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('order/', views.order, name='order'),
    path('address/', views.address, name='address'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptop-data'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomwear-data'),
    path('invertor/', views.invertor, name='invertor'),
    path('invertor/<slug:data>', views.invertor, name='invertor-data'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='addo/login.html',authentication_form=LoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='addo/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='addo/passwordchangedone.html'), name='passwordchangedone'),

#    path('login/', views.login, name='login'),
    path('registration/',views.CustomerRegistrationView.as_view(), name="customerregistration"),



    path('techworld/', views.techworld, name='techworld'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
