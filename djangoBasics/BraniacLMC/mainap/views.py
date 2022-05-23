from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
from django.urls import resolve
from datetime import datetime, timedelta
import json


# def check_kwargs(request, **kwargs):
#     return HttpResponse(f'kwargs:<br>{kwargs}')
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
        with open('mainap/templates/mainap/news.json') as file:
            stock = json.load(file)
        context['json_news'] = stock
        context['object_list'] = [
            {
                'news_title': 'Первый новостной заголовок',
                'news_text': 'Первый новостной текст',
                'news_number': 1,
                'news_date': datetime.now()
            }, {
                'news_title': 'Второй новостной заголовок',
                'news_text': 'Второй новостной текст',
                'news_number': 2,
                'news_date': datetime.now() - timedelta(1)
            }, {
                'news_title': 'Третий новостной заголовок',
                'news_text': 'Третий новостной текст',
                'news_number': 3,
                'news_date': datetime.now() - timedelta(2)
            }, {
                'news_title': 'Четвертый новостной заголовок',
                'news_text': 'Четвертый новостной текст',
                'news_number': 4,
                'news_date': datetime.now() - timedelta(3)
            }, {
                'news_title': 'Пятый новостной заголовок',
                'news_text': 'Пятый новостной текст',
                'news_number': 5,
                'news_date': datetime.now() - timedelta(4)
            }
        ]
        return context


class NewsPageViewWithPaginator(NewsPageView):

    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context


class CoursesPageView(TemplateView):
    template_name = 'mainap/courses_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = [
            {
                'course_picture': 'img/course001.jpg',
                'course_name': 'Web Python',
                'course_number': 1
            }, {
                'course_picture': 'img/course002.jpg',
                'course_name': 'Web Golang',
                'course_number': 2
            }, {
                'course_picture': 'img/course003.jpg',
                'course_name': 'Web JavaScript',
                'course_number': 3
            }, {
                'course_picture': 'img/course004.jpg',
                'course_name': 'Web Java',
                'course_number': 4
            }, {
                'course_picture': 'img/course005.jpg',
                'course_name': 'Web PHP',
                'course_number': 5
            }, {
                'course_picture': 'img/course006.jpg',
                'course_name': 'Python AI',
                'course_number': 6
            }, {
                'course_picture': 'img/course007.jpg',
                'course_name': 'DevOps',
                'course_number': 7
            }
        ]
        return context


class ContactsPageView(TemplateView):
    template_name = 'mainap/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'email': 'geeklab@spb.ru',
                'address': 'территория Петропавловская крепость, 3'
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@kz.ru',
                'address': 'территория Кремль, 11, Казань, Республика Татарстан, Россия'
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email': 'geeklab@msk.ru',
                'address': 'Красная площадь, 7, Москва, Россия'
            }
        ]
        return context


class DocSitePageView(TemplateView):
    template_name = 'mainap/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainap/login.html'
