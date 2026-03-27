from django.contrib import admin
from django.urls import path
from myapp.views import home, about, contact

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('admin/', admin.site.urls),
]
