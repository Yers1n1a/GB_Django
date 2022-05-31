from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from authap.models import User


class LoginPageView(TemplateView):
    template_name = 'authap/login.html'


class RegisterView(TemplateView):
    template_name = 'authap/register.html'

    def post(self, request, *args, **kwargs):
        try:
            if all(
                    (
                        request.POST.get('username'),
                        request.POST.get('password'),
                        request.POST.get('password2'),
                        request.POST.get('first_name'),
                        request.POST.get('last_name'),
                        request.POST.get('password') == request.POST.get('password2'),
                        request.POST.get('email'),
                    )
            ):
                new_user = User.objects.create(
                    username=request.POST.get('username'),
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    email=request.POST.get('email'),
                    age=request.POST.get('age') if request.POST.get('age') else 0,
                    avatar=request.FILES.get('avatar')
                )
                new_user.set_password(request.POST.get('password'))
                new_user.save()
                messages.add_message(request, messages.INFO, 'Регистрация прошла успешно')
                return HttpResponseRedirect(reverse('authap:login'))
            else:
                messages.add_message(request, messages.WARNING, 'Что-то пошло не так')
                return HttpResponseRedirect(reverse('authap:register'))
        except Exception as ex:
                messages.add_message(request, messages.WARNING, new_user)
                return HttpResponseRedirect(reverse('mainap:main_page'))

class LogoutView(TemplateView):
    pass


class EditView(TemplateView):
    pass




# class CustomLoginView(LoginView):
#     def form_valid(self, form):
#         ret = super().form_valid(form)
#         message = _("Login success!<br>Hi, %(username)s") % {
#         "username": self.request.user.get_full_name()
#         if self.request.user.get_full_name()
#         else self.request.user.get_username()
#         }
#         messages.add_message(self.request, messages.INFO, mark_safe(message))
#         return ret
#
#     def form_invalid(self, form):
#         for _unused, msg in form.error_messages.items():
#             messages.add_message(
#             self.request,
#             messages.WARNING,
#             mark_safe(f"Something goes worng:<br>{msg}"),
#             )
#         return self.render_to_response(self.get_context_data(form=form))
