from django.forms import ModelForm, fields, models
from apps.Quizzes.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'imagen')
        

