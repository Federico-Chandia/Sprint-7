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
from api import views as api_views
from Clientes import views as cliente_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_de_jaqueo.LoginView.as_view()),
    path('Tarjetas/', tarjetas_views.Tarjeta, name="tarjetas"),
    path('Prestamos/', prestamo_views.prestamo, name="prestamos"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',login_views.registro, name="registro"),
    path('Cuentas/', views.Cuenta, name= "cuentas"),
    path('api/', api_views.SucursalesLists.as_view(), name= "api_sucursales"),
    path('api/borrar_prestamo/<str:pk>/', api_views.DelPrestamos.as_view(), name = 'api_borrar_prestamo'),
    path('api/<int:cliente_id>/', cliente_views.ClienteDetails.as_view(), name= "api_cliente_details"),
    path('api/prestamo/', api_views.Create_prestamo.as_view(), name= "api_create_prestamo"),
    path('api/saldo/<int:pk>/', api_views.SaldoDetails.as_view(), name="api_saldo_details"),
    path('api/cliente/<int:customer_dni>/',api_views.TarjetasDeCliente.as_view(), name="api_cliente_tarjetas"),
    path('api/cliente/direccion/<int:customer_dni>/',api_views.CambiarDireccionCliente.as_view(), name="api_cliente_direccion"),
    path('api/prestamo/cliente/<int:reqDNI>/',api_views.PrestamosRetrieve.as_view(), name="api_monto_prestamo_cliente")



]
