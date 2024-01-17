from django.contrib import admin
from django.urls import path,include
from mysite import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('jet/',include('jet.url','jet')),
    path('admin/', admin.site.urls),
    path('',include('home.url')),
    path('category',include('category.url')),
    path('about',include('about.url')),
    path('login',include('login.url')),
    path('Register',include('Register.url')),
    path('contact',include('contact.url')),
    path('Mobile',include('Mobile.url')),
    path('listing',include('listing.url')),
    path('form',include('form.url')),
    path('categories',include('categories.url')),
    path('privacy',include('privacy.url')),
    path('fulldetail',include('fulldetail.url')),
    path('mobile',include('mobile.url')),
    path('people',include('people.url')),
    path('mobile',include('mobile.url')),

]
urlpatterns += static(settings.MEDIA_URL,document_roots=settings.MEDIA_ROOT)
