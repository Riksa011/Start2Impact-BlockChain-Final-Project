from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin url
    path('admin/', admin.site.urls),
    # blocksneakers app url
    path('', include('blocksneakers.urls')),
]
