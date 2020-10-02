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
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comment = post.comments.filter(active=True)
    new_comment = None
    #Comment posted

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {
    'post': post,
    'comment': comment,
    'new_comment': new_comment,
    'comment_form': comment_form
    })

def about_page(request):
    template_name = 'about_page.html'
    return render(request, template_name)

def contact_page(request):
    template_name = 'contact_page.html'

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            email_contact = request.POST.get('email_contact', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information

            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'email_contact': email_contact,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "myblog"+'',['test@test.com'], 
                headers = {'Reply-to': email_contact}
            )
            email.send()
            messages.success(request, "E-mail sent with success")
            return redirect('contact_page')
    
    return render(request, template_name, {'form': ContactForm})


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == 'GET':
        return render (
            request, 'users/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse('home'))