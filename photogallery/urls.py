"""Gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_page,name='index_page'),

    path('accounts/register/',views.register,name='register'),
    path('accounts/profile/',views.profile,name='profile'),
    path('accounts/profile/delete/<int:photo_id>/',views.delete_photo,name='delete_photo'),
    path('accounts/profile/favorite/<int:photo_id>/',views.favorite_photo,name='favorite_photo'),
    path('accounts/profile/view/<int:photo_id>/favorite/',views.view_favorite_photo,name='view_favorite_photo'),

    path('accounts/profile/import/',views.import_photo,name="import"),
    path('accounts/profile/archive/',views.archive,name='archive'),
    
    path('accounts/profile/view/<int:photo_id>/',views.view_photo,name="view_photo"),
    path('accounts/profile/add/<int:photo_id>/',views.add_photo,name='add_photo'),
]


