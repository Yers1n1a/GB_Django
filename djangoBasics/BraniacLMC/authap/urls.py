from authap.apps import AuthapConfig
from django.urls import path
from authap.views import LoginPageView, RegisterView, LogoutView, EditView

app_name = AuthapConfig.name

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LogoutView.as_view(), name='logout'),
    # path('login/', EditView.as_view(), name='edit'),
]