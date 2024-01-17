"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('category',views.category,name='category'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('Register',views.Register,name='Register'),
    path('contact',views.contact,name='contact'),
    path('form',views.form,name='form'),
    path('categories',views.categories,name='categories'),
    path('privacy',views.privacy,name='privacy'),
    path('fulldetail', views.fulldetail, name="fulldetail"),
    path('view', views.view, name="view"),
    path('mobile', views.mobile, name="mobile"),
    path('people', views.people, name="people")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)