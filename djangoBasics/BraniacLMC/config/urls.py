"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mainap import views
from mainap.apps import MainapConfig
from django.views.generic import RedirectView

app_name = MainapConfig.name

urlpatterns = [
    path('', RedirectView.as_view(url='mainap/')),
    path('mainap/', include('mainap.urls', namespace='mainap')),
    path('admin/', admin.site.urls),
    path('authap/', include('authap.urls', namespace='authap'))
]

# добавляется для работы джанго с медиа
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
