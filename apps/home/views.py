import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#@login_required(login_url='/authentication/login')
def home(request):
    # Si se envía una solicitud POST, actualizar el idioma en la sesión
    if request.method == 'POST':
        request.session['language'] = request.POST.get('language', 'English')
    
    # Cargar el archivo JSON con la configuración de idioma
    with open('language.json', 'r', encoding='utf-8') as file:
        language_data = json.load(file)
    
    # Determinar el idioma seleccionado por el usuario
    selected_language = request.session.get('language', 'English')
    
    # Obtener los datos del idioma seleccionado para la página de inicio
    menu_header = language_data[selected_language]['home']['menu_header']
    home_text = language_data[selected_language]['home']['text']
    home_button = language_data[selected_language]['home']['button']

    # Crear el contexto con los datos cargados
    context = {
        'menu_header': menu_header,
        'text': home_text,
        'button_text': home_button
    }
    return render(request, 'home/home.html', context)

