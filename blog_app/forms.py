from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm

#Formulário de comentários
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

#Formulário de contato
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    email_contact = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = 'Your name: '
        self.fields['email_contact'].label = 'Your email: '
        self.fields['content'].label = 'What would you like to say? '

#Formulário de registro de usuário
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)