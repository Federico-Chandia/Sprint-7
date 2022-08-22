"""homebanking URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Login import views as login_views
from django.conf import settings
from django.conf.urls.static import static
from Tarjetas import views as tarjetas_views
from Prestamos import views as prestamo_views
from Cuentas import views as cuentas_views
from django.urls import include
from Cuentas import views 
from django.contrib.auth import views as views_de_jaqueo



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_de_jaqueo.LoginView.as_view()),
    path('Tarjetas/', tarjetas_views.Tarjeta, name="tarjetas"),
    path('Prestamos/', prestamo_views.prestamo, name="prestamos"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',login_views.registro, name="registro"),
    path('Cuentas/', views.Cuenta, name= "cuentas"),



]
