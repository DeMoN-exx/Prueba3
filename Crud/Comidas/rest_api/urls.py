
from django.urls import path
from . import views

urlpatterns=[
    path('menu_list',views.menu_list,name="menu_list"),
    path('local_list',views.local_list,name="local_list"),
    path('menu_detail/<id>',views.menu_detail,name="menu_detail"),
    path('local_detail/<id>',views.local_detail,name="local_detail"),
    path('login',views.login,name="login"),
]