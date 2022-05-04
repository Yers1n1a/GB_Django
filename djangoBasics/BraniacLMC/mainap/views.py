from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView


# def check_kwargs(request, **kwargs):
#     return HttpResponse(f'kwartgs:<br>{kwargs}')
#
#
# class HeloWorldView(View):
#     def get(self, *args):
#         return HttpResponse('Hello World!')


class MainPageView(TemplateView):
    template_name = 'mainap/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainap/news.html'


class CoursesPageView(TemplateView):
    template_name = 'mainap/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainap/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainap/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainap/login.html'