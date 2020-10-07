from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Estado de criação dos posts
STATUS = (
(0, 'draft'), 
(1, 'publish')
)

#Classe que cria as tabelas no BD
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='static/img/', blank=True, null=True)

    #classe meta para ordenação do conteúdo
    class Meta:
        ordering = ['-created_on']

    #Função para mostrar o conteúdo por titulo
    def __str__(self):
        return self.title

#Classe que cria as tabelas com conteúdo dos comentários no BD
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    #classe meta para ordenação do conteúdo
    class Meta:
        ordering = ['-created_on']
    
    #Função para mostrar o conteúdo por comentário e nome
    def __str__(self):
        return f'Comment {self.body} by {self.name}'