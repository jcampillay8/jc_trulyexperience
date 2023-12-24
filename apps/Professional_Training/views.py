from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Professional_Training
from .forms import ProfessionalTrainingForm

def professional_training(request):
    professional_trainings = Professional_Training.objects.all()
    return render(request, "Professional_Training/professional_training.html", {'professional_trainings':professional_trainings})

def add_professional_training(request):
    if request.method == 'POST':
        form = ProfessionalTrainingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cargado exitosamente')
            return redirect('professional_training')
        else:
            messages.error(request, 'Carga Fallida')
    else:
        form = ProfessionalTrainingForm()
    return render(request, 'Professional_Training/add_professional_training.html', {'form': form})