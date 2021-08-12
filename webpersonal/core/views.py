from django.shortcuts import render, HttpResponse

html_base = """
<h1> Mi web personal</h1>
<u1>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</u1>
"""
def home(request):
    return HttpResponse(html_base + """
    <h1>Mi web personal</h1>
    <h2>Portada</2>
    """)

def about(request):
    return HttpResponse(html_base + """
    <h2>Acerca de</2>
    <p>Soy Diego y soy programador</p>
    """)

def portfolio(request):
    return HttpResponse(html_base + """
    <h2>Portfolio</2>
    <p>Hola esto es un portfolio</p>
    """)
def contact(request):
    return HttpResponse(html_base + """
    <h2>Contact</2>
    <p>Este es mi contacto</p>
    """)
# Create your views here.
