from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('details/<date>/', views.details, name='details'),
    path('details/<date>/<int:id>/', views.book, name='book'),
    path('details/<date>/<int:id>/book/', views.book_request, name='book_request'),
]
