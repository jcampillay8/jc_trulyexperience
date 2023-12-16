import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from guest_user.decorators import allow_guest_user
from django.contrib.auth.mixins import LoginRequiredMixin



def welcome(request):
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
    home_button_guest = language_data[selected_language]['home']['button_guest']
    home_button_authenticated = language_data[selected_language]['home']['button_authenticated']

    # Crear el contexto con los datos cargados
    context = {
        'menu_header': menu_header,
        'text': home_text,
        'button_guest': home_button_guest,
        'button_authenticated':home_button_authenticated,
    }
    return render(request, 'welcome.html', context)


#@allow_guest_user
@login_required(login_url='/authentication/login')
def home(request):
#    pass
    print('Nombre Usuario: '+ str(request.user))
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    elif request.user.is_guest:
        return render(request, 'home/home.html')
    else:
        # Redirigir a la página de inicio de sesión si no es ni invitado ni registrado
        return redirect('/authentication/login')


# @login_required(login_url='/authentication/login')
# def home(request):
#     # Si se envía una solicitud POST, actualizar el idioma en la sesión
#     if request.method == 'POST':
#         request.session['language'] = request.POST.get('language', 'English')
    
#     # Cargar el archivo JSON con la configuración de idioma
#     with open('language.json', 'r', encoding='utf-8') as file:
#         language_data = json.load(file)
    
#     # Determinar el idioma seleccionado por el usuario
#     selected_language = request.session.get('language', 'English')
    
#     # Obtener los datos del idioma seleccionado para la página de inicio
#     menu_header = language_data[selected_language]['home']['menu_header']
#     home_text = language_data[selected_language]['home']['text']
#     home_button = language_data[selected_language]['home']['button']

#     # Crear el contexto con los datos cargados
#     context = {
#         'menu_header': menu_header,
#         'text': home_text,
#         'button_text': home_button
#     }
#     return render(request, 'home/home.html', context)

