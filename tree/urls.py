"""tree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from tree_app import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('tree_app.urls')),
    #path('',views.login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('home/',views.home, name='home'),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('tree/<int:book_id>', views.tree, name='tree'),
    path('write_tree/<str:node_id>/<int:book_id>', views.write_tree, name='write_tree'),
    path('read_tree/<str:node_id>/<int:book_id>', views.read_tree, name='read_tree'),
]
