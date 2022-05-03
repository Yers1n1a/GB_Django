from django.contrib import admin
from django.urls import path, include
from mainap import views
from mainap.apps import MainapConfig

app_name = MainapConfig.name

urlpatterns = [
    path('', views.MainPageView.as_view()),
    path('news/', views.NewsPageView.as_view()),
    path('courses/', views.CoursesPageView.as_view()),
    path('contacts/', views.ContactsPageView.as_view()),
    path('doc_site/', views.DocSitePageView.as_view()),
    path('login/', views.LoginPageView.as_view()),
]