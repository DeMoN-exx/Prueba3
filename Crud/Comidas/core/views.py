from django.shortcuts import render, redirect
from .models import Comida, Local 
from .form import ComidaForm
# Create your views here.
def main (request):
    comentario ={"titulo":"COMENTARIO ENVIADO DESDE DJANGO A LA PAGINA"}
    return render(request, "core/main.html", comentario)

def menu (request):
    context ={}
    return render (request, 'core/menu.html', context)

def locales (request):
    return render(request, "core/locales.html")     

def carrito (request):
    return render(request, "core/carrito.html")

def login(request):
    return render(request,"core/admin/login.html")

def checkout(request):
    return render(request,"core/admin/checkout.html")

#CREAR TANTAS FICHAS COMO PÁGINAS TENGA 
def detalle1comida (request):
    return render(request, "core/detalle1comida.html")

def detalle2comida (request):
    return render(request, "core/detalle2comida.html")

def detalle3comida (request):
    return render(request, "core/detalle3comida.html")

def detalle4comida (request):
    return render(request, "core/detalle4comida.html")

def detalle1local (request):
    return render(request, "core/detalle1local .html")

def detalle2local (request):
    return render(request, "core/detalle2local .html")

def detalle3local (request):
    return render(request, "core/detalle3local .html")

def indexadmin(request):
    comida = Comida.objects.all()
    local = Local.objects.all()
    conext ={"comida":comida, "local":local}
    return render(request,"core/admin/indexadmin.html", conext)

def save_comida(request):
    form=ComidaForm
    mensaje = ""

    if request.method == 'POST':
        form = ComidaForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = request.POST.get('nombre', None)
            if nombre in Comida.objects.values_list('nombre', flat=True):
                mensaje = "Esta comida ya existe en la base de datos, intente con otra."
            else:
                form.save()
                mensaje = "Datos guardados con éxito."
    return render(request,"core/admin/save_comida.html",{"mensaje": mensaje,"form":form})

def mod_comida(request, id):
    comida=Comida.objects.get(nombre=id)
    mensaje = ""
    if request.method == 'POST':
        form = ComidaForm(request.POST, request.FILES, instance=comida)
        if form.is_valid():
            form.save()
            mensaje = "Datos modificados con éxito"
            return redirect(to="indexadmin")
    return render(request, "core/admin/mod_comida.html",{"form":ComidaForm(instance=comida), "mensaje":mensaje})

def delete_comida(request, id):
    comida = Comida.objects.get(nombre=id)
    comida.delete()
    return redirect(to="indexadmin")