from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Professional_Studies
from .forms import ProfessionalStudiesForm

def professional_studies(request):
    levels = request.GET.getlist('levels')  # Esto obtendrá una lista de los niveles seleccionados
    
    #language = request.session.get('language', 'English')  # Obtén el idioma de la sesión, por defecto es 'English'
    if request.method == 'POST':
        request.session['language'] = request.POST.get('language', 'English')

    

    if levels:
        professional_studies = Professional_Studies.objects.filter(level__in=levels).order_by('-date')
    else:
        professional_studies = Professional_Studies.objects.all().order_by('-date')

    # Crear una lista para almacenar los estudios profesionales con el idioma correcto
    professional_studies_translated = []

    for study in professional_studies:
        context = {}
        context['date'] = study.date
        context['image'] = study.image
        context['level'] = study.level

        if request.session['language'] == 'English':
            context['title'] = study.title
            context['subtitle'] = study.subtitle
            context['content'] = study.content
        else:
            context['title'] = study.titulo
            context['subtitle'] = study.subtitulo
            context['content'] = study.contenido

        professional_studies_translated.append(context)

    return render(request, "Professional_Studies/professional_studies.html", {'professional_studies': professional_studies_translated, 'selected_levels': levels})




def add_professional_studies(request):
    if request.method == 'POST':
        form = ProfessionalStudiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cargado exitosamente')
            return redirect('professional_studies')
        else:
            messages.error(request, 'Carga Fallida')
    else:
        form = ProfessionalStudiesForm()
    return render(request, 'Professional_Studies/add_professional_studies.html', {'form': form})