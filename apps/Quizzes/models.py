# models.py
from django.contrib.auth.models import User
from django.db import models
from django.views.decorators.csrf import csrf_exempt

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=11)
    title = models.CharField(max_length=None)
    description = models.CharField(max_length=None)
    imagen = models.ImageField(upload_to='imagenes/', default='imagen')
    likes = models.ManyToManyField(User, related_name='post_likes')

    def cantidad_likes(self):
        return self.likes.count()

class Question(models.Model):
    question_text = models.CharField(max_length=None)
    explanation = models.TextField()
    home_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)  # Agregamos una relación con Post

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=None)
    is_correct = models.BooleanField(default=False)

class UserQuestionValue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, default=None)
    value = models.IntegerField(default=10)


@csrf_exempt
def update_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_id = data.get('question_id')
        new_question_text = data.get('question_text')
        new_choices = data.get('choices')

        # Encuentra la pregunta y actualiza el texto
        question = Question.objects.get(id=question_id)
        question.question_text = new_question_text
        question.save()

        # Encuentra las opciones y actualiza el texto
        for i, new_choice_text in enumerate(new_choices):
            choice = Choice.objects.get(question=question, id=i)
            choice.choice_text = new_choice_text
            choice.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})