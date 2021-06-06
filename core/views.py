from django.shortcuts import render, HttpResponse
html_base = """<h1>Mi web personal Jose Manuel</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/portfolio">Portafolio</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>    
"""
# Create your views here.
def home(request):
    #return HttpResponse("<h1>Mi web personal JoseMa</h1><h2>Portada</h2>")
    #return HttpResponse(html_base + """<h2>Portada</h2>
    #<p>Bienvenido(a) a mi pagina personal</p>
    #""")
    return render(request,"core/home.html")

def about(request):
    #return HttpResponse(html_base + """<h2>Acerca de mi</h2>
    #<p>Me llamo Jose Manuel y soy desarrollador</p>
    #""") 
    return render(request,"core/about-me.html")

def portafolio(request):
    return render(request,"core/portfolio")

def contacto(request):
    return render(request,"core/contact.html")