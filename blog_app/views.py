from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post
from .forms import CommentForm, ContactForm, CustomUserCreationForm
from django import template
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login

# Create your views here.
#classe para retornar os posts
class PostList(generic.ListView):
    #queryset para filtrar o objetos por publicados e decescente
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    #variável guardando a página index
    template_name = 'index.html'
    #inserir 3 osts por página
    paginate_by = 3

#Função com o que contém no post
def post_detail(request, slug):
    #variável guardando a página de post
    template_name = 'post_detail.html'
    #variável guardando o objeto(post) ou erro 404 caso não encontrado
    post = get_object_or_404(Post, slug=slug)
    #variável guardando os comentários
    comment = post.comments.filter(active=True)
    #variável guardando um novo comentário vazio
    new_comment = None    
    #Se o request for um método POST
    if request.method == 'POST':
        #variável guardando o formulário de comentário
        comment_form = CommentForm(data=request.POST)
        #Se o formulário de comentário for válido
        if comment_form.is_valid():
            #Cria um objeto de comentário mas não o salva
            new_comment = comment_form.save(commit=False)
            #Atrela o novo comentário ao post
            new_comment.post = post
            # Salva o comentário ao BD
            new_comment.save()
    else:
        #Se não, apenas retorna o formulário de comentário
        comment_form = CommentForm()
    #Retorna o post com os comentários antigos e novos    
    return render(request, template_name, {
    'post': post,
    'comment': comment,
    'new_comment': new_comment,
    'comment_form': comment_form
    })
#Função da página sobre
def about_page(request):
    #variável guardando a página sobre
    template_name = 'about_page.html'
    #retorna a página sobre
    return render(request, template_name)

#Função da página contato
def contact_page(request):
    #variável guardando a página contato
    template_name = 'contact_page.html'
    #Se o request for um método POST
    if request.method == 'POST':
        #Variável guardando o formulário de contato
        contact_form = ContactForm(data=request.POST)
        #Se o formulário for válido
        if contact_form.is_valid():
            #guarda o nome do contato
            contact_name = request.POST.get('contact_name', '')
            #guarda o email do contato
            email_contact = request.POST.get('email_contact', '')
            #guarda o conteúdo do contato
            form_content = request.POST.get('content', '')
            #guarda o template de contato em modo txt
            template = get_template('contact_template.txt')
            #contexto para ser chamado no html da página com os dados
            context = {
                'contact_name': contact_name,
                'email_contact': email_contact,
                'form_content': form_content,
            }
            #renderiza os dados do contexto
            content = template.render(context)
            #guarda as informações de resposta de email
            email = EmailMessage(
                "New contact form submission",
                content,
                "myblog"+'',['test@test.com'], 
                headers = {'Reply-to': email_contact}
            )
            #retorna a resposta de confirmaçao do envio do email
            email.send()
            messages.success(request, "E-mail sent with success")
            return redirect('contact_page')
    #retorna a página de contato
    return render(request, template_name, {'form': ContactForm})
    
#Função de registro de usuário
def register(request):
    #Se o request for um método GET
    if request.method == 'GET':
        #retorna a página de registro com o formulário de registro
        return render (
            request, 'users/register.html',
            {'form': CustomUserCreationForm}
        )
    #Se o método for POST
    elif request.method =='POST':
        #guarda o formulário de registro
        form = CustomUserCreationForm(request.POST)
        #Se o formulário for válido
        if form.is_valid():
            #salva o usuário
            user = form.save()
            #faz o login
            login(request, user)
        #retorna para a página home 
        return redirect(reverse('home'))