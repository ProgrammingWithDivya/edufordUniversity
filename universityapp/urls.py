from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('course/',views.course,name='course'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('comment/',views.comment,name='comment'),
    path('saveEnquiry/',views.saveEnquiry,name='saveEnquiry'),
    path('logout/', views.logout_view, name='logout'),  # Add the logout URL
]