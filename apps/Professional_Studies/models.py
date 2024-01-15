from django.db import models

LEVEL_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
]

#Create your models here.
class Professional_Studies(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título", null=True, default='')
    title = models.CharField(max_length=200, verbose_name="Title")
    subtitulo = models.CharField(max_length=200, verbose_name="Subtítulo", null=True, default='')
    subtitle = models.CharField(max_length=200, verbose_name="Subtitle")
    contenido = models.TextField(verbose_name="Contenido", null=True, default='')
    content = models.TextField(verbose_name="Content")
    date = models.DateField(auto_now_add=False, verbose_name="Fecha")
    image = models.ImageField(verbose_name="Imagen", upload_to="professional_studies")
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1, verbose_name="Nivel")
    website = models.URLField(max_length=200, verbose_name="Website", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "professional_studies"
        verbose_name_plural = "professional_studies"
        ordering = ['-created']

    def __str__(self):
        return self.title