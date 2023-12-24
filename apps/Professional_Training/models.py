from django.db import models

LEVEL_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
]

# Create your models here.
class Professional_Training(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    date = models.DateField(auto_now_add=False, verbose_name="Fecha")
    image = models.ImageField(verbose_name="Imagen", upload_to="professional_training")
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1, verbose_name="Nivel")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "professional_training"
        verbose_name_plural = "professional_trainings"
        ordering = ['-created']

    def __str__(self):
        return self.title