from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
from django.urls import resolve


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = [
            {
                'news_title': 'Первый новостной заголовок',
                'news_text': 'Первый новостной текст'
            },{
                'news_title': 'Второй новостной заголовок',
                'news_text': 'Второй новостной текст'
            },{
                'news_title': 'Третий новостной заголовок',
                'news_text': 'Третий новостной текст'
            },{
                'news_title': 'Четвертый новостной заголовок',
                'news_text': 'Четвертый новостной текст'
            },{
                'news_title': 'Пятый новостной заголовок',
                'news_text': 'Пятый новостной текст'
            }
        ]
        return context


class CoursesPageView(TemplateView):
    template_name = 'mainap/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainap/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainap/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainap/login.html'