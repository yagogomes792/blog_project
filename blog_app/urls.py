from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name ='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('about', views.about_page, name='about_page'),
    path('contact', views.contact_page, name='contact_page'),
]