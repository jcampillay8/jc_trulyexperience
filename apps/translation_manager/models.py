# from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import User
# import datetime
# from django.utils.timezone import now


# class Expense(models.Model):
#     name = models.CharField(max_length=255, db_index=True, default='')
#     date = models.DateField(default=now)
#     amount = models.FloatField(blank=False, null=False)
#     currency = models.CharField(max_length=20, default="USD")
#     category = models.CharField(max_length=255)
#     owner = models.ForeignKey(
#         to=User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['-date']


# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     class Meta:
#         verbose_name_plural = "Categories"

#     def __str__(self):
#         return self.name










# from django.db import models

# class TranslationKey(models.Model):
#     key = models.CharField(max_length=255)

#     def __str__(self):
#         return self.key

# class Translation(models.Model):
#     translation_key = models.ForeignKey(TranslationKey, on_delete=models.CASCADE)
#     language = models.CharField(max_length=30)
#     translation = models.TextField()

#     def __str__(self):
#         return f'{self.translation_key.key} ({self.language})'






# from django.db import models

# class Tabla1(models.Model):
#     columna2 = models.CharField(max_length=200)
#     columna3 = models.CharField(max_length=200)
#     # Agrega más campos según sea necesario

# class Tabla2(models.Model):
#     foreign_key = models.ForeignKey(Tabla1, on_delete=models.CASCADE)
#     english = models.CharField(max_length=200)
#     spanish = models.CharField(max_length=200)


# from django.db import models
# from django.db.models import JSONField

# class TranslationKey(models.Model):
#     key = models.CharField(max_length=255)

#     def __str__(self):
#         return self.key

# class TranslationValue(models.Model):
#     translation_key = models.ForeignKey(TranslationKey, on_delete=models.CASCADE)
#     english_value = JSONField()
#     spanish_value = JSONField()

#     def __str__(self):
#         return f"{self.translation_key.key}"














# from django.db import models
# from django.contrib.postgres.fields import JSONField

# class Translation(models.Model):
#     key = models.CharField(max_length=255)
#     english_value = JSONField()
#     spanish_value = JSONField()

#     def __str__(self):
#         return self.key
