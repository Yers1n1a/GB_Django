from django.contrib import admin
from django.urls import path, include
from mainap import views
from mainap.apps import MainapConfig
from django.views.generic import RedirectView

app_name = MainapConfig.name

urlpatterns = [
    path('', RedirectView.as_view(url='index.html')),
    path('index.html', views.MainPageView.as_view(), name='main_page'),
    path('news/', views.NewsPageView.as_view(), name='news'),
    path('courses/', views.CoursesPageView.as_view(), name='courses'),
    path('contacts/', views.ContactsPageView.as_view(), name='contacts'),
    path('doc_site/', views.DocSitePageView.as_view(), name='doc_site'),
    path('login/', views.LoginPageView.as_view(), name='login'),
]