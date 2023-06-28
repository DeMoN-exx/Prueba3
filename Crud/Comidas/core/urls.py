from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.main, name="main"),
    path('locales/',views.locales, name="locales"),
    path('menu/',views.menu, name="menu"),
    path('login/',LoginView.as_view(template_name="core/admin/login.html"),name="login"),
    path('logout/',LogoutView.as_view(template_name="core/main.html"),name="logout"),
    path('indexadmin/',views.indexadmin, name="indexadmin"),
    path('carrito/',views.carrito, name="carrito"),
    path('checkout/',views.checkout, name="checkout"),
    path('save_comida',views.save_comida, name="save_comida"),
    path('mod_comida/<id>',views.mod_comida, name="mod_comida"),
    path('delete_comida/<id>',views.delete_comida, name="delete_comida"),
    path('detalle1comida',views.detalle1comida, name="detalle1comida"),
    path('detalle2comida',views.detalle2comida, name="detalle2comida"),
    path('detalle3comida',views.detalle3comida, name="detalle3comida"),
    path('detalle4comida',views.detalle4comida, name="detalle4comida"),
    path('detalle1local',views.detalle1local, name="detalle1local"),
    path('detalle2local',views.detalle2local, name="detalle2local"),
    path('detalle3local',views.detalle3local, name="detalle3local"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)